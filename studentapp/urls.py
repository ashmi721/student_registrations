from django.urls import path
from studentapp.views import home,user_register,user_login,user_profile,user_logout
urlpatterns = [
    path("", home),
    path("register/",user_register,name='register_page'),
    path("login/",user_login,name="login_page"),
    path("profile/",user_profile,name="profile_page"),
    path("logout/",user_logout,name="logout_page"),
   
]
