
# Django
from django.conf import settings
from django.contrib.auth.backends import BaseBackend

# models
from .models import GuestUser


class CustomBackend(BaseBackend):
    """
    Authentication system with only email to register an order for 
    GuestUser
    """

    def authenticate(self, request, email=None):
        if email is not None:
            try:
                user = GuestUser.objects.get(email=email)
                return user
            except GuestUser.DoesNotExist:
                raise 'El usuario no existe'
        return email

    def get_user(self, email):
        try:
            user = GuestUser.objects.get(email=email)
            return {'email': user.email, 'id': user.id}
        except GuestUser.DoesNotExist:
            return None
