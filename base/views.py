from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from urllib import request
from django.contrib.auth.forms import UserCreationForm
from base.models import *

# Create your views here.
def Home(request):
    return render(request,'base/home.html')

def Cart(request):
    return render(request,'base/cart.html')

def Billing(request):
    return render(request,'base/billing.html')

def Login(request):
    return render(request,'base/login.html')

def Product(request):
    return render(request,'base/product.html')

# creating usercreation form
def signupPage(request):
    if request.method=='POST':
        email=request.POST.get('email')
        username=request.POST.get('username')
        name= request.POST.get('name')
        password=request.POST.get('password')
        user=User.objects.create(username=username,email=email,password=password)
        user.name=name
        # user.lastname=lastname1
        user.save()
    

    return render(request,'base/signup.html')