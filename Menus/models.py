# Django
from django.db import models
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.shortcuts import render


# others
import humanize

# uuid
import uuid

from django.db.models.deletion import CASCADE


class Menu(models.Model):

    uuid = models.UUIDField(
        default=uuid.uuid4, primary_key=True, editable=False)

    date = models.DateField(unique=True)
    admin_user = models.ForeignKey(User, on_delete=CASCADE)

    option_1 = models.CharField(max_length=50, blank=False)
    option_2 = models.CharField(max_length=50, blank=False)
    option_3 = models.CharField(max_length=50, blank=False)
    option_4 = models.CharField(max_length=50, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    send = models.BooleanField(default=False)

    def __str__(self):
        date = str(humanize.naturaldate(self.date))
        return date

    @classmethod
    def filter_menu(self, uuid):
        return self.objects.get(uuid=uuid)

    @classmethod
    def menu_register(self, data, admin_user):
        menu = Menu()
        menu.date = data['date']
        menu.option_1 = data['option_1']
        menu.option_2 = data['option_2']
        menu.option_3 = data['option_3']
        menu.option_4 = data['option_4']
        menu.admin_user = admin_user
        menu.save()

    @classmethod
    def all_menus(self, admin_user_id):
        menus = self.objects.all().filter(admin_user_id=admin_user_id).order_by('date')
        return menus

    @classmethod
    def update(self, data, uuid):
        menu = self.objects.get(uuid=uuid)
        menu.option_1 = data['option_1']
        menu.option_2 = data['option_2']
        menu.option_3 = data['option_3']
        menu.option_4 = data['option_4']

        menu.save()
