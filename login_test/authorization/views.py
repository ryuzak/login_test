# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse

from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout

from accounts.models import User

# Create your views here.
def account_login(request):
    message = ''
    login_form = LoginForm(request.POST or None)

    if login_form.is_valid():
        user = authenticate(email=login_form.cleaned_data.get('email'), password=login_form.cleaned_data.get('password'))
        if user and user.is_active:
            login(request, user)
            return redirect('authorization:dashboard')
        else:
            message = 'Correo o contraseña no validos 1'
    else:
        message= 'Correo o contraseña no validos 2'
    
    return render(request, 'authorization/login.html',{'form': login_form, 'message' : message})

def account_logout(request):    
    logout(request)
    # Take the user back to the login
    return HttpResponseRedirect('/login')

def account_dashboard(request):
    if(request.user.is_authenticated()):
        return render(request, 'authorization/dashboard.html', {'user':request.user})
    else:
        return redirect('authorization:login')


