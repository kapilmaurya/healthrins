from select import select
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from urllib import request
from django.contrib import messages
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
        user_obj=User.objects.filter(username=email)
        if user_obj.exists():
            messages.warning(request,'Email is already taken')
            return HttpResponseRedirect(request.path_info)

        user=User.objects.create(username=username,email=email,password=password)
        user.name=name
        # user.lastname=lastname1
        user.save()
    

    return render(request,'base/signup.html')

def product(request):
    product=Product.objects.all()
    return render(request,'base/product.html',context = {'product' : product})
def orderPage(request):
    return render(request,'base/billing.html',)

def privacyPage(request):
    return render(request,'base/privacypolicy.html')
def termsPage(request):
    return render(request,'base/terms&condition.html')
def returnPage(request):
    return render(request,'base/returnrefund.html')