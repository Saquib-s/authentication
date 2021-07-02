# Create your views here.
from django.shortcuts import render, redirect
from . models import ExtendUser
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(reuest):
    return render (reuest,'home.html')

def dashboard(reuest):
    return render (reuest,'dashboard.html')

def signup(request):
    if request.method == 'POST':
        username= request.POST['username']
        email= request.POST['email']
        password1= request.POST['password1']
        password2= request.POST['password2']
        phone = request.POST['phone']
        if password1 != password2:
            messages.error(request, 'password do not match')
            return redirect('/signup/')
        if User.objects.filter(username=username).exists():
            messages.error(request,'Username taken')
            return redirect('/signup/')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('/signup/')
        else:
            user=User.objects.create_user( username=username,email=email,password=password1)
            extend = ExtendUser(phone=phone,_id=user)
            extend.save()
            return redirect('/login/')


    return render (request,'signup.html')


def Login(request):
    if request.method=="POST":

        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request,'invalid credentials')
            return redirect('/login/')

    return render(request,'login.html')


def Logout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/login/')