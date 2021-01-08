from django.db.models.deletion import CASCADE
from Users.models import GuestUser
from django.db import models

# Create your models here.


class Order(models.Model):
    guest_user = models.ForeignKey(GuestUser, on_delete=CASCADE)

    menu_option = models.IntegerField(blank=False)

    description_order = models.CharField(blank=True, max_length=30)

    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)
