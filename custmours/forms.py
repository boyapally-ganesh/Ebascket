from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class customuserform(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'username'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'con_password'}))
    class Meta:
        model = User
        fields = ['username','email','password1','password2']