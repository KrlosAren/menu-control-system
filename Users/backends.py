from Users.models import GuestUser
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.exceptions import MultipleObjectsReturned
from django.db.models import Q


class GuestBackend(ModelBackend):
    def authenticate(self, request, username=None, **kwargs):
        try:
            guest_user = GuestUser.objects.filter(email=username)
        except MultipleObjectsReturned:
            return GuestUser.objects.get(email=username)
        else:
            if self.user_can_authenticate(guest_user):
                return guest_user
