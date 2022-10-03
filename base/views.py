from multiprocessing import context
import re
from select import select
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from urllib import request, response
from django.contrib import messages
from base.models import *
from base.models import Order_items
from base.forms import CreateUserForm
# from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def Home(request):
    product=Product.objects.get()
    pack_select=request.POST.get('pack-select')
    print(pack_select)
    return render(request,'base/home.html',context = {'product' : product})

def Cart(request):
    return render(request,'base/cart.html')

def Billing(request):
    return render(request,'base/billing.html')

def Login(request):
    return render(request,'base/login.html')

# creating usercreation form
# def signupPage(request):
#     form = UserCreationForm()
#     context={'form':form}
#     
#     return render(request,'base/signup.html',context)
    # if request.method=='POST':
    #     email=request.POST.get('email')
    #     username=request.POST.get('username')
    #     name= request.POST.get('name')
    #     password=request.POST.get('password')
    #     user_obj=User.objects.filter(username=email)
    #     if user_obj.exists():
    #         messages.warning(request,'Email is already taken')
    #         return HttpResponseRedirect(request.path_info)

    #     user=User.objects.create(username=username,email=email,password=password)
    #     user.name=name
    #     # user.lastname=lastname1
    #     user.save()
    

def signupPage(request):
    form=CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print('form not valid')
    context={'form':form}
    return render(request,'base/account.html',context)


def product(request):
    product=Product.objects.get()
    if request.method=='POST':
        pack_select=request.POST.get('pack-select')
        quantity=request.POST.get('quantity')
        Order_items.objects.create(product_id=product,quantity=quantity,pack_selection=pack_select)
        print(Order_items)
        return render(request,'base/billing.html')
    return render(request,'base/product.html',context = {'product' : product})
def orderPage(request):
    order_items=Order_items.objects.all()
    print(order_items.pack_Selection)
    # if request.method=='POST':
    return render(request,'base/billing.html',context ={'order' : order_items})

def privacyPage(request):
    return render(request,'base/privacypolicy.html')
def termsPage(request):
    return render(request,'base/terms&condition.html')
def returnPage(request):
    return render(request,'base/returnrefund.html')

def contactPage(request):
    return render(request,'base/contact.html')