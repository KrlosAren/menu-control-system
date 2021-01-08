# Django
from django.contrib import admin

# Menu Model
from Menus.models import Menu

# register menus in admin module
admin.site.register(Menu)
