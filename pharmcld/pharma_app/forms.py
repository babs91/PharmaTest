from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from .models import customers, customer_orders, adminEntry


class CreateUserForm(UserCreationForm):

   class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileForm(ModelForm):

    class Meta:
        model = customers
        fields = ['first_name', 'Tel', 'email', 'address', 'profile_Pic']


class CustorderForm(ModelForm):

    class Meta:
        model = customer_orders
        fields = '__all__'


class entryForm(ModelForm):

    class Meta:
        model = adminEntry
        fields = '__all__'