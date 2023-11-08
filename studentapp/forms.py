from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder":""}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": ""}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": ""}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"class": "form-control", "placeholder": ""}))
    city = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": ""}))
    address = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": ""}))
    contact = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": ""}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={"class": "form-control", "placeholder": ""}))
    conform_password = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={"class": "form-control", "placeholder": ""}))        
