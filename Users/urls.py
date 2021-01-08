from os import name
from django.urls import path
from .views import login_view, register_view, home

urlpatterns = [


    path('login/', login_view, name='login_view'),
    path('register/', register_view, name='register_view'),
]
