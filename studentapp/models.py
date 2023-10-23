from django.db import models

# Create your models here.
class Student(models.Model):
    first_name= models.CharField(max_length=20) 
    last_name= models.CharField(max_length=40)
    username = models.CharField(max_length=20)
    email = models.EmailField()
    city = models.CharField(max_length=50)
    age = models.IntegerField()
    address=models.CharField(max_length=100)
    contact=models.CharField(max_length=14)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
def __str__(self):
    return self.username