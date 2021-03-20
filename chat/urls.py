from django.urls import path
from . import views

urlpatterns = [
    path('',views.login, name='login'),
    path('index/' , views.index , name='index'),
    path('signup/',views.signup, name='signup'),
    path('logout/',views.logout, name='logout'),
    path('chat/<int:id>/', views.chat, name='create_room'),
]
