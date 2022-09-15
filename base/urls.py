from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home,name='home'),
    path('cart/', views.Cart),
    path('billing/', views.Billing),
    path('login/', views.Login,name='login'),
    path('product/', views.Product,name='product'),
    path('signup/', views.signupPage,name='signup'),
]