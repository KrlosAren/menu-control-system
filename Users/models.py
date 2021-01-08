from django.db import models

# Create your models here.


class GuestUser(models.Model):

  email = models.EmailField(max_length=50, blank=False)
  first_name = models.CharField(max_length=50, blank=False)

  created_at = models.DateTimeField(auto_now_add=True)
  last_login = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.email