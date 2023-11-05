from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Student(models.Model):
#     first_name= models.CharField(max_length=20) 
#     last_name= models.CharField(max_length=40)
#     username = models.CharField(max_length=20)
#     email = models.EmailField()
#     city = models.CharField(max_length=50)
#     address=models.CharField(max_length=100)
#     contact=models.CharField(max_length=14)
#     password=models.CharField(max_length=16)
#     conf_password=models.CharField(max_length=16,default='')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    
    

# Create your models here.
class Profile(models.Model):
    student = models.ForeignKey(User,on_delete=models.CASCADE)
    contact = models.CharField(max_length=14,default='98')
    address = models.CharField(max_length=50, default='')
    city = models.CharField(max_length=50, default='')
    profile_pic = models.CharField(max_length=150, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
      return self.student.username