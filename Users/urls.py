from django.urls import path
from .views import login_view, register_view, logout_view, admin_home

urlpatterns = [

    # admin home
    path('home/', admin_home, name='admin_home'),

    # admin login | register | logout
    path('login/', login_view, name='login_view'),
    path('register/', register_view, name='register_view'),
    path('logout/', logout_view, name='logout'),
]
