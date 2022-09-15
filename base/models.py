from xml.parsers.expat import model
from django.db import models

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=500)
    price=models.DecimalField(max_digits=4,decimal_places=2)
    pack=models.CharField(max_length=100)
    sku=models.DecimalField(max_digits=3,decimal_places=2)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class User(models.Model):
    Username=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)
    First_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    telephone=models.DecimalField(max_digits=10,decimal_places=2)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)

class User_payments(models.Model):
    user_id=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    payment_type=models.CharField(max_length=100)
    account_no=models.DecimalField(max_digits=3,decimal_places=2)

class Address(models.Model):
    user_id=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    address_line1=models.CharField(max_length=200)
    address_line2=models.CharField(max_length=200)
    postal_code=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    telephone=models.DecimalField(max_digits=10,decimal_places=2)
    mobile=models.DecimalField(max_digits=10,decimal_places=2)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)

class Shopping_session(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    total=models.DecimalField(max_digits=3,decimal_places=2)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)

class Cart(models.Model):
    session_id=models.ForeignKey(Shopping_session, on_delete=models.CASCADE, null=True)
    product_id=models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity=models.DecimalField(max_digits=3,decimal_places=2)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)

class Order_items(models.Model):
    # order_id=models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    product_id=models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity=models.DecimalField(max_digits=3,decimal_places=2)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)

class Order_details(models.Model):
    User_id=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    total=models.DecimalField(max_digits=3,decimal_places=2)
    # payment_id=models.ForeignKey()
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)
