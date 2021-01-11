from django.contrib.auth import get_user
from Menus.models import Menu
from django.db.models.deletion import CASCADE
from Users.models import GuestUser
from django.db import models

# Create your models here.


class Order(models.Model):
    """

    Order Model 

    for this model the following methods have been added

    - register_order: to make more easy add a order to DB
    - get_all_by_guest: retrieves all orders by customer to prevent two or more
                        orders by menu for customer.
    - get_orders_by_admin_user: raw query to retrieves all orders by admin 

    """

    menu_id = models.ForeignKey(Menu, on_delete=CASCADE)
    guest_user = models.ForeignKey(GuestUser, on_delete=CASCADE)
    menu_option = models.IntegerField(blank=False)
    description_order = models.CharField(blank=True, max_length=30)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)

    def __str__(self):
        return str(self.guest_user)

    @classmethod
    def register_order(self, guest, uuid, data, list_menu):
        if uuid in list_menu:
            return False
        else:
            order = Order()
            order.guest_user_id = guest
            order.description_order = data['description_order']
            order.menu_option = data['menu_option']
            order.menu_id_id = uuid
            order.save()
            return True

    @classmethod
    def get_all_by_guest(self, guest_user_id):
        menus = self.objects.values('menu_id_id').all().filter(
            guest_user_id=guest_user_id)
        return [str(menu['menu_id_id']) for menu in menus]

    @classmethod
    def get_orders_by_admin_user(self,admin_id):
        orders = self.objects.raw('''
            SELECT 
            m.date  AS date,
            u.first_name AS name,
            o.menu_option AS menu,
            o.description_order AS description,
            o.id AS id,
            o.created_at AS order_date
            FROM 
            Menus_menu as m 
            JOIN auth_user as ad
            ON
            m.admin_user_id = ad.id
            JOIN
            Users_guestuser as u 
            JOIN Orders_order as o 
            ON u.id= o.guest_user_id WHERE m.admin_user_id=%s
            GROUP BY m.date 
            ORDER BY o.created_at
            ;
        ''', [admin_id])
        return orders

