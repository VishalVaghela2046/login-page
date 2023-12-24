from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
# from .forms import *

# Create your views here.

def home(request):
    return render(request,'authentication/index.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        mailid = request.POST['mailid']
        passwd = request.POST['passwd']
        
        
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist!")
            return redirect('home')
            
        if User.objects.filter(email=mailid):
            messages.error(request,"Email id is already registered.")
            return redirect('home')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('home')
        
        
        myuser = User.objects.create_user(username,mailid,passwd)
        myuser.get_full_name = username
        myuser.is_active = False
        myuser.is_active =True
        myuser.save()
        messages.success(request, "Your Account has been created succesfully!!")
        
        
        
        
        
        return redirect('signin')
        
    return render(request, "authentication/signup.html")

 
def signin(request): 
    if request.method == 'POST':
        username = request.POST['username']
        passwd = request.POST['passwd']
        
        user = authenticate(username=username,password=passwd)
        
        if user is not None:
            login(request, user)
            name = user.username
            print("User Authenticated Successfully!")
            return render(request, "authentication/index.html",{"name":username})
        
        else:
            messages.error(request,"Username or Password Incorrect!!!")
            return redirect('home')
            
        
        
    return render(request, 'authentication/signin.html')

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('home')

    


