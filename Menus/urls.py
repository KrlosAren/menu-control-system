"""

    Menu Urls ,

    Aqui se encontraran las Url asociadas a al sistema de Menu

    - Creacion
    - Lectura
    - Actualizacion
    - Eliminacion

    """

# Django
from django.urls import path

# Orders views
from .views import menu_register, menu_update, menu_delete, menu_list

urlpatterns = [
    path('register/', menu_register, name='menu_register_view'),
    path('update/<uuid>', menu_update, name='menu_update_view'),
    path('delete/<uuid>', menu_delete, name='menu_delete_view'),
    path('list/', menu_list, name='menu_list_view'),

]
