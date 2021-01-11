# django
from datetime import datetime
from django.contrib.auth.models import User
from django.test.testcases import TestCase


# models
from ..models import Menu


class TestMenuModel(TestCase):

    def test_model_create(self):
        user = User()
        user.save()
        data = {
            'date': '2021-10-10',
            'option_1': 'Potato',
            'option_2': 'Pear',
            'option_3': 'Corn',
            'option_4': 'Rice with Chicken',
        }
        menu = Menu.menu_register(
            data=data,
            admin_user=user
        )
        self.assertEqual(menu, data)

    def test_update_method(self):
        user = User()
        user.save()
        data = {
            'date': '2021-10-10',
            'option_1': 'Potato',
            'option_2': 'Pear',
            'option_3': 'Corn',
            'option_4': 'Rice with Chicken',
        }
        menu = Menu.menu_register(
            data=data,
            admin_user=user
        )
        menu.update(data={
            'option_1': 'Batatas al horno'
        }
        )

        self.assertEqual(data['option_1'], menu['option_1'])

    def test_get_all_menus(self):
      user = User()
      menu = Menu()
      menus = menu.all_menus(user)
      self.assertTrue(len(menus) >= 0)

