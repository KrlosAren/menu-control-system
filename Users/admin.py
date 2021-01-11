# Django
from django.contrib import admin
from django.contrib.auth.models import User
# Models
from .models import GuestUser


admin.site.register(GuestUser)
