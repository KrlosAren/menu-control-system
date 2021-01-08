# Django modules
from django import forms

# models from meal -


class OrderRegisterForm(forms.Form):

    menu_option = forms.CharField(max_length=6, required=True)
    description_order = forms.CharField(required=False, max_length=30)

    
