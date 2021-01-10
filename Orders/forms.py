# Django modules
from django import forms

# models from meal -


class OrderRegisterForm(forms.Form):

    email = forms.EmailField(required=True, min_length=5, max_length=50, widget=forms.EmailInput(attrs={
        'class':  'form-control'
    }))
    first_name = forms.CharField(required=True, min_length=2, max_length=50, widget=forms.TextInput(attrs={
        'class':  'form-control'
    }))

    menu_option = forms.CharField(max_length=6, required=True, widget=forms.TextInput(attrs={
        'class':  'form-control'
    }))
    description_order = forms.CharField(required=False, max_length=30, widget=forms.TextInput(attrs={
        'class':  'form-control'
    }))
