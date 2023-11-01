from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Student,Profile
from .helper import save_file
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
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
        contact=request.POST.get("contact") 
        password=request.POST.get("password") 
        conf_password=request.POST.get("conf_password") 
        
        if password != conf_password:
            error = "Password and Conform Password field doesn't match"
            messages.error(request,error)
            return redirect("/register")
        
       # Check if the username or email already exists
        existing_user = Student.objects.filter(username=username).exists()    
        existing_email = Student.objects.filter(email=email).exists()

        if existing_user or existing_email:
            error = "Username or Email already exists"
            messages.error(request, error)
            return redirect("/register")
        
        else:
            # If the user or email does not exist, create a new Student object
           student = Student.objects.create(
            first_name=first_name, 
            last_name=last_name,
            username=username,
            email=email,
            city=city,
            address=address,
            contact=contact, 
            )
          # Set the password for the student
           student.set_password(password)
           student.save()
           
           profile_data={
            "student":student,   
            "profile_pic":"https://png.pngitem.com/pimgs/s/111-1114675_user-login-person-man-enter-person-login-icon.png"
                }
           profile=Profile.objects.create(**profile_data)
           return redirect("/login")    
    return render(request,"studentapp/register.html",context={"title":"registrations"})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # print("Username: ", username, "Password: ", password)
       
        check_user = Student.objects.filter(username=username).first()
        print(check_user)
        if check_user is None:
            error = "Account does not exist"
            messages.error(request, error)
            return redirect("/login")

        is_valid_user = authenticate(username=username, password=password)
        print(is_valid_user)
        if is_valid_user:
            login(request, is_valid_user)
            request.session["name"] = is_valid_user.first_name
            return redirect("/profile")
        else:
            error = "Invalid username or password"
            messages.error(request, error)
            return redirect("/login")
    return render(request,"studentapp/login.html")


@login_required
def user_profile(request):
    # Student_id = request.student.pk
    # profile= Profile.objects.get(student_id=Student_id)
    return render(request,"studentapp/profile.html",)