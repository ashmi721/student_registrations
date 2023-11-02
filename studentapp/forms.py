from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "Enter First Name"}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "Enter Last Name"}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "Enter Username"}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"class": "form-control", "placeholder": "Enter Email"}))
    city = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "Enter City"}))
    address = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "Enter Address"}))
    contact = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "Enter Contact"}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={"class": "form-control", "placeholder": "Enter Password"}))
    conform_password = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={"class": "form-control", "placeholder": "Repeat your Password"}))        
