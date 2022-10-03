from dataclasses import fields
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
    class Meta:
        model= User
        fields=['username','email','password1','password2']
        # widgets = {
        #         'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
        #         # 'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
        #         # 'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
        #         'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        #         'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        #         'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}),
        #     }
