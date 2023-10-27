from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login
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
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print("Username: ", username, "Password: ", password)
        check_user = Student.objects.filter(username=username)
        if not check_user.exists():
            error = "Account does not exists"
            messages.error(request, error)
            return redirect("/login")
        is_valid_user = authenticate(username=check_user[0].username, password=password)
        if is_valid_user:
            login(request,is_valid_user)
            # request.session["name"] = is_valid_user.first_name
            return redirect("/register")
        else:
            error = "Invalid Username or Password"
            messages.error(request, error)
            return redirect("/login")
    return render(request,"studentapp/login.html")