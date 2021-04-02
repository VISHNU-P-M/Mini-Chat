from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User, auth
import uuid
from .models import *
# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect(index)
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return JsonResponse('true',safe=False)
            else:
                return JsonResponse('false',safe=False)
        return render(request, 'login.html')
    
def signup(request):
    if request.user.is_authenticated:
        return redirect(index)
    else:
        if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            print(username,email,password)
            if User.objects.filter(username=username).exists():
                return JsonResponse('user',safe=False)
            elif User.objects.filter(email=email).exists():
                return JsonResponse('email',safe=False)
            else:
                User.objects.create_user(username=username,email=email,password=password)
                return JsonResponse('true',safe=False)
        else:
            return redirect(login)

def index(request):
    if request.user.is_authenticated:
        admin = request.user
        users = User.objects.filter().exclude(id=request.user.id)
        return render(request, 'index.html',{'users':users,'admin':admin})
    else:
        return redirect(login)
    
def chat(request,id):
    if request.user.is_authenticated:
        user1 = request.user
        user2 = User.objects.get(id=id)
        if OneToOne.objects.filter(user1=user1,user2=user2).exists():
            onetoone = OneToOne.objects.get(user1=user1,user2=user2)
            room_name = onetoone.room_name
        elif OneToOne.objects.filter(user1=user2,user2=user1).exists():
            onetoone = OneToOne.objects.get(user1=user2,user2=user1)
            room_name = onetoone.room_name
        else:
            room_name = uuid.uuid1()
            onetoone = OneToOne.objects.create(user1=user1,user2=user2,room_name=room_name) 
        messages = Messages.objects.filter(onetoone__room_name=room_name)
        context = {'room_name':room_name,'user':user1,'receiver':user2,'messages':messages}
        return render(request, 'chatroom.html',context)
    else:
        return redirect(login)


def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect(login)