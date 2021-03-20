from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class OneToOne(models.Model):
    user1 = models.ForeignKey(User,on_delete=models.CASCADE,related_name='%(class)s_requests_created')
    user2 = models.ForeignKey(User,on_delete=models.CASCADE,related_name='%(class)s_requests_reciever') 
    room_name = models.CharField(max_length=100)
    
class Messages(models.Model):
    sender = models.ForeignKey(User,on_delete=models.CASCADE,related_name='%(class)s_requests_sender')
    receiver = models.ForeignKey(User,on_delete=models.CASCADE,related_name='%(class)s_requests_reciever')
    onetoone = models.ForeignKey(OneToOne,on_delete=models.CASCADE)
    date = models.DateTimeField()
    message = models.TextField()
    