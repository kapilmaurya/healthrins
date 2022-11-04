from email import message
from multiprocessing import context
from select import select

from unicodedata import name
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from urllib import request, response
from django.contrib import messages
from base.models import *
from base.models import Order_items
from base.forms import CreateUserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import razorpay
# from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def Home(request):
    product=Product.objects.get()
    pack_select=request.POST.get('pack-select')
    print(pack_select)
    return render(request,'base/home.html',context = {'product' : product})

def Cart(request):
    return render(request,'base/cart.html')

def Login(request):
    if request.method=='POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            # messages.warning(request,'User is Login')
            context={'user':user}
            return redirect('home')
        else:
            messages.warning(request,'Not Signup yet')
    return render(request,'base/login.html')

def Logout(request):
    logout(request)
    # messages.warning(request,'Logout')
    return redirect('home')

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
            user=form.cleaned_data.get('username')
            messages.success(request,'Account is Created for '+user)
            return redirect('Login')

        else:
            messages.error(request,'Password Must Contain ')
    context={'form':form}
    return render(request,'base/account.html',context)


def product(request):
    product=Product.objects.get()
    order_item=Order_items.objects.all()
    if request.method=='POST':
        if request.user.is_authenticated:
            live_user=request.user
            pack_select=request.POST.get('pack-select')
            quantity=int(request.POST.get('quantity'))
            if pack_select=='1':
                price=product.price*quantity
            elif pack_select=='2':
                price=product.pack2*quantity
            else:
                price=product.pack3*quantity
            order_item=Order_items.objects.create(product_id=product,quantity=quantity,pack_selection=pack_select,price=price)
        # print(Order_items)
            return redirect('orderpage',order_item.id)
        else:
            return redirect('signup')
    return render(request,'base/product.html',context = {'product' : product,'order_item':order_item})

@login_required(login_url='login/')
def orderPage(request,id):
    order_item=Order_items.objects.get(id=id)
    print(order_item.price)
    od_id=Order_items.objects.all()
    user=request.user
    # razorpay payment gateway
    DATA = {
        "amount": order_item.price*100,
        "currency": "INR",
        "payment_capture":1
    }
    client = razorpay.Client(auth=("rzp_test_IIQTmTylnnMUkg", "WWMTFLtlL683eVVmelNyZUoK"))
    payment=client.order.create(data=DATA)
    print(payment)
    Order_details.objects.create(user= user ,order_id=payment['id'], total=payment['amount'])

    return render(request,'base/billing.html',context ={'order' : order_item , 'payment':payment})

def privacyPage(request):
    return render(request,'base/privacypolicy.html')
def termsPage(request):
    return render(request,'base/terms&condition.html')
def returnPage(request):
    return render(request,'base/returnrefund.html')

def contactPage(request):
    return render(request,'base/contact.html')

def successPage(request):
    return render(request,'base/PaymentSucces.html')