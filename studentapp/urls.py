from django.urls import path
from .views import home,user_register,user_login,user_profile
urlpatterns = [
    path("", home),
    path("register/",user_register,name='register_page'),
    path("login/",user_login,name="login_page"),
    path("profile/",user_profile,name="profile_page"),
   
]
