# from tkinter import CASCADE
from email.policy import default
from xml.parsers.expat import model
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=500)
    price=models.DecimalField(max_digits=7,decimal_places=2)
    pack2=models.IntegerField(default=20)
    pack3=models.IntegerField(default=30)
    sku=models.DecimalField(max_digits=3,decimal_places=2)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Profile(models.Model):
    User=models.OneToOneField(User,on_delete=models.CASCADE)
    username=models.CharField(max_length=100)
    email=models.CharField(max_length=200,unique=True)
    name=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)
    # telephone=models.DecimalField(max_digits=10,decimal_places=2)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)


# class Account(UserCreationForm):
#     Username=models.CharField(max_length=100)
#     Password=models.CharField(max_length=100)
#     First_name=models.CharField(max_length=100)
#     last_name=models.CharField(max_length=100)
#     telephone=models.DecimalField(max_digits=10,decimal_places=2)
#     created_at=models.DateTimeField(auto_now=True)
#     updated_at=models.DateTimeField(auto_now=True)

# class User_payments(models.Model):
#     user_id=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     payment_type=models.CharField(max_length=100)
#     account_no=models.DecimalField(max_digits=3,decimal_places=2)

class Address(models.Model):
    user_id=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    First_name=models.CharField(max_length=100,default='abc')
    last_name=models.CharField(max_length=100, default='abc')
    address_line1=models.CharField(max_length=200)
    address_line2=models.CharField(max_length=200)
    postal_code=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    telephone=models.DecimalField(max_digits=10,decimal_places=2)
    mobile=models.DecimalField(max_digits=10,decimal_places=2)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)

# class Shopping_session(models.Model):
#     user_id=models.ForeignKey(User,on_delete=models.CASCADE, null=True)
#     total=models.DecimalField(max_digits=3,decimal_places=2)
#     created_at=models.DateTimeField(auto_now=True)
#     updated_at=models.DateTimeField(auto_now=True)

class Cart(models.Model):
    user_id=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product_id=models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity=models.DecimalField(max_digits=3,decimal_places=2)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)

class Order_items(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    product_id=models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity=models.DecimalField(max_digits=3,decimal_places=2)
    pack_selection= models.IntegerField(default=1)
    # pack=models.CharField(max_length=20)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return (f"{self.pk} {self.product_id}")

# class Order_details(models.Model):
#     User_id=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     total=models.DecimalField(max_digits=3,decimal_places=2)
#     # payment_id=models.ForeignKey()
#     created_at=models.DateTimeField(auto_now=True)
#     updated_at=models.DateTimeField(auto_now=True)
