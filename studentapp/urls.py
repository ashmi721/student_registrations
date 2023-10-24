from django.urls import path
from .views import home,user_register,user_login
urlpatterns = [
    path("", home),
    path("register/",user_register,name='register_page'),
   
    path("login/",user_login,name="login_page"),
    
   
]
