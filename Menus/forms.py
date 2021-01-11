"""Menu forms."""

# Django
from django import forms


class MenuRegister(forms.Form):
    """
      Menu register form
      recieves 
      - date
      - 4 menus options all is required

    """

    date = forms.DateField(required=True)
    option_1 = forms.CharField(max_length=50, required=True)
    option_2 = forms.CharField(max_length=50, required=True)
    option_3 = forms.CharField(max_length=50, required=True)
    option_4 = forms.CharField(max_length=50, required=True)


class MenuUpdate(forms.Form):
    """
    Menu update form

    recieves
    - 4 menu options
     

    """
    option_1 = forms.CharField(max_length=50, required=True)
    option_2 = forms.CharField(max_length=50, required=True)
    option_3 = forms.CharField(max_length=50, required=True)
    option_4 = forms.CharField(max_length=50, required=True)
