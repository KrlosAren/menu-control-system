from django.db import models

# Create your models here.


class GuestUser(models.Model):

    email = models.EmailField(max_length=50, blank=False, unique=True)
    first_name = models.CharField(max_length=50, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email

    @classmethod
    def get_user(self, email):
        user = self.objects.values(
            'id', 'email', 'first_name').filter(email=email)
        if user is not None:
            return user
        else:
            return False

    @classmethod
    def create_guest_user(self, data):
        users = self.get_all()
        if data['email'] in users:
            return self.get_user(email=data['email'])
        else:
            self.objects.create(
                email=data['email'], first_name=data['first_name'])
            return self.get_user(data['email'])

    @classmethod
    def get_all(self):
        users = self.objects.all()
        return [user.email for user in users]
