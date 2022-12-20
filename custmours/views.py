from django.shortcuts import render, redirect, HttpResponseRedirect
from products .models import Category, product
from .models import profile
from django.contrib import messages
from .forms import customuserform
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.contrib.auth.models import User
import random
# from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
# Create your views here.
def register(request):
    form = customuserform()
    if request.method == 'POST':
        form = customuserform(request.POST)
        if form.is_valid():
            form.save()
            message = 'registered successfully ! login to continue'
            return redirect('/login/')
            messages.success(request, message)
    context = {'form':form}
    return render(request, "custmour/signup.html", context)
def auth_login(request):
    if not request.user.is_authenticated:
      if request.method == 'POST':
         lg = AuthenticationForm(request=request, data=request.POST)
         if lg.is_valid():
            uname=lg.cleaned_data['username']
            upass=lg.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
               login(request, user)
               messages.success(request, 'logged in successfully')
              
               return HttpResponseRedirect('/')
      else:
        messages.error(request, 'invalid username or password')
        lg = AuthenticationForm()
      return render(request, 'custmour/login.html')
    else:
        messages.warning(request, "you are already logged in")
        return HttpResponseRedirect('/')
def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'logged out successfully')
    return redirect('/')
login_required(login_url='login')
def account(request):
    myprofile = profile.objects.filter(user=request.user)
    context = {'profile':myprofile}
    return render(request, 'custmour/account.html', context)
def address(request):
    myaddress = profile.objects.filter(user=request.user)
    context = {'address':myaddress}
    return render(request, 'custmour/address.html',context)
# def orders(request):
#     return render(request, 'custmour/orders.html')