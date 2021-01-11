
# django
from django.test import TestCase

class TestUrls(TestCase):

  def test_menu_register(self):
    response = self.client.get('/menu/register')
    self.assertEqual(response.status_code, 301)

  def test_menu_update(self):
    response = self.client.get('/menu/update/<uuid>')
    self.assertEqual(response.status_code, 302)

  def test_menu_delete(self):
    response = self.client.get('/menu/delete/<uuid>')
    self.assertEqual(response.status_code, 302)

  def test_menu_list(self):
    response = self.client.get('/menu/list')
    self.assertEqual(response.status_code, 301)

  def test_menu_send(self):
    response = self.client.get('/menu/send/<uuid>')
    self.assertEqual(response.status_code, 302)
