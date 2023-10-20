from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("hello world")

def user_register(request):
    # return HttpResponse("this is register page")
    return render(request,"studentapp/register.html",context={"title":"registrations"})

def user_login(request):
    return render(request,"studentapp/login.html")