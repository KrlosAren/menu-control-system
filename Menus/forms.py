"""Menu forms."""

# Django
from django.http import request
from Menus.models import Menu
from django import forms


class MenuRegister(forms.Form):
    """
      Form para registro del menu

    """

    date = forms.DateField(required=True)
    option_1 = forms.CharField(max_length=50, required=True)
    option_2 = forms.CharField(max_length=50, required=True)
    option_3 = forms.CharField(max_length=50, required=True)
    option_4 = forms.CharField(max_length=50, required=True)


class MenuUpdate(forms.Form):
    """
    Updated menu form without date
    """
    option_1 = forms.CharField(max_length=50, required=True)
    option_2 = forms.CharField(max_length=50, required=True)
    option_3 = forms.CharField(max_length=50, required=True)
    option_4 = forms.CharField(max_length=50, required=True)
