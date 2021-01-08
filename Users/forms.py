"""User forms."""

# Django
from django.contrib.auth import authenticate
from Users.models import GuestUser
from django import forms

# Models
from django.contrib.auth.models import User


class SignupForm(forms.Form):
    """Sign up form."""

    username = forms.CharField(min_length=4, max_length=50)

    password = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )
    password_confirmation = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )

    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50)

    email = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.EmailInput()
    )

    def clean_username(self):
        """Username must be unique."""
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('Username is already in use.')
        return username

    def clean(self):
        """Verify password confirmation match."""
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match.'):

        return data

    def save(self):
        """Create user."""
        data = self.cleaned_data
        data.pop('password_confirmation')

        User.objects.create_user(**data)


class GuestForm(forms.Form):
    """Guest Form

    Form para registrar a los usuarios que solicitan el menu 
    y asociarlos a algun correo
    """

    email = forms.EmailField(required=True, min_length=5, max_length=50)
    first_name = forms.CharField(required=True, min_length=2, max_length=50)

    def clean_email(self):
        """
        confirmar que el correo ya esta registrado,
        si lo estas devolver el user
        """

        email = self.cleaned_data['email']
        email_taken = GuestUser.objects.filter(email=email).exists()
        if email_taken:
            guest_user = authenticate(email=email)
        else:
            guest_user = GuestUser.objects.create(email=email)
        return email
    
    def save()