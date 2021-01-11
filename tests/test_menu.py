"""
    Testing Menu module CRUD
    """

# django
from django.contrib.auth.models import User
from django.test import TestCase

# json
import json

# models
from ..Menus.models import Menu

class MenuTestCase(TestCase):
    def setUp(self):

        admin_user = User.objects.create(
          username='testUserCase',
            
          )

        data = {
            "date": "2021-12-01",
            "option_1": "Corn pie, Salad , Dessert",
            "option_2": "Chicken Nugget Rice, Salad, Dessert",
            "option_3": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            "option_4": "Premium chicken, Salad ,Dessert."
        }
        Menu.menu_register(data=data, admin_user=admin_user)

    def test_menu(self):
      admin_user = 9
      menu = Menu().all_menus(admin_user_id=admin_user)

      self.assertEqual(menu['option_1'], 'Corn pie, Salad , Dessert')


