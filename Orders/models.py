from Menus.models import Menu
from django.db.models.deletion import CASCADE
from Users.models import GuestUser
from django.db import models


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
            return
        else:
            self.objects.create(
                guest_user_id=guest,
                description_order=data['description_order'],
                menu_option=data['menu_option'],
                menu_id_id=uuid,
            )
            return

    @classmethod
    def get_all_by_guest(self, guest_user_id):
        menus = self.objects.values('menu_id_id').all().filter(
            guest_user_id=guest_user_id)
        return [str(menu['menu_id_id']) for menu in menus]

    @classmethod
    def get_orders_by_admin_user(self, admin_id):
        orders = self.objects.raw('''SELECT
                                    u.id,
                                    m.date,
                                    u.first_name as name,
                                    o.menu_option as menu,
                                    o.description_order as description,
                                    o.created_at as order_date
                                    FROM 
                                    Orders_order AS o 
                                    JOIN
                                    Menus_menu AS m
                                    ON
                                    m.uuid = o.menu_id_id 
                                    JOIN 
                                    auth_user AS ad
                                    ON 
                                    ad.id = m.admin_user_id
                                    JOIN 
                                    Users_guestuser AS u
                                    ON
                                    u.id=o.guest_user_id
                                    WHERE ad.id=%s
                                    GROUP BY
                                    m.date
                                    ORDER BY
                                    o.created_at
                                            ''', [admin_id])
        return orders
