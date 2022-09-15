from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

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
    form=UserCreationForm()
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            # user.username=user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
            # print('bhr hu')
        else:
            message.error(request,'error while registering')
    context={'form':form}       
    return render(request,'base/signup.html',context)
