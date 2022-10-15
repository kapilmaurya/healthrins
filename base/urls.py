from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home,name='home'),
    path('cart/', views.Cart),
    path('login/', views.Login,name='login'),
    path('logout/', views.Logout,name='logout'),
    path('product/', views.product,name='product'),
    path('signup/', views.signupPage,name='signup'),
    path('Billing/', views.orderPage,name='orderpage'),
    path('privacypolicy/', views.privacyPage,name='privacypolicy'),
    path('terms&conditions/', views.termsPage,name='terms&conditions'),
    path('returnrefund/', views.returnPage,name='returnrefund'),
    path('contact/', views.contactPage,name='contact'),

]