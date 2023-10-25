from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student
# Create your views here.
def home(request):
    return HttpResponse("hello world")

def user_register(request):
    if request.method == 'POST':
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username=request.POST.get("username") 
        email=request.POST.get("email")
        city=request.POST.get("city")
        address=request.POST.get("address")
        age=request.POST.get("age")
        contact=request.POST.get("contact") 
        password=request.POST.get("password")
        
        Student.objects.create(first_name=first_name,last_name=last_name,username=username,email=email,city=city,address=address,age=age,contact=contact,password=password)
        return redirect("/login")
    return render(request,"studentapp/register.html",context={"title":"registrations"})

def user_login(request):
    return render(request,"studentapp/login.html")