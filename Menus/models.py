# Django
from django.db import models
from django.contrib.auth.models import User

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
        date = humanize.naturaldate(self.date)
        return date

    def update_menu(self, data, admin_user, uuid):
        import pdb; pdb.set_trace()
        self.date = data['date']
        self.option_1 = data['option_1']
        self.option_2 = data['option_2']
        self.option_3 = data['option_3']
        self.option_4 = data['option_4']
        self.admin_user = admin_user
        self.save()
