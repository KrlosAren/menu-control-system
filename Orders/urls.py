"""

    Orders Urls ,

    Aqui se encontraran las Url asociadas a las ordenes de menus

    """

# Django
from django.urls import path

# Orders views
from .views import order_register, order_save

urlpatterns = [
    path('register/', order_register, name='order_register_view'),
    path('save/', order_save, name='order_save'),
]
