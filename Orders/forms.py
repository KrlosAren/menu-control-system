# Django modules
from django import forms
from django.forms.widgets import NumberInput

"""
Use this forms to save customer user and order.
If client  exists the form only have the menu and order
else the form have a inputs form email and firstname

"""


class OrderRegisterWithUser(forms.Form):

    email = forms.EmailField(required=True, min_length=5, max_length=50, widget=forms.EmailInput(attrs={
        'class':  'form-control'
    }))
    first_name = forms.CharField(required=True, min_length=2, max_length=50, widget=forms.TextInput(attrs={
        'class':  'form-control'
    }))
    menu_option = forms.IntegerField(required=True , max_value=4)

    description_order = forms.CharField(required=False, max_length=30, widget=forms.TextInput(attrs={
        'class':  'form-control'
    }))


class OrderRegisterForm(forms.Form):

    menu_option = forms.CharField(max_length=6, required=True, widget=forms.TextInput(attrs={
        'class':  'form-control'
    }))
    description_order = forms.CharField(required=False, max_length=30, widget=forms.TextInput(attrs={
        'class':  'form-control'
    }))
