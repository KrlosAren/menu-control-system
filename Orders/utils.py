"""
      Utils for Order module

        this function can register the customer if it is not in the database
        if the customer is in DB save the order associated with the customer.
        Both functions save cookies to remind the user of the email and not
        request this information again.

    """


from Orders.models import Order
from Users.models import GuestUser


def order_user_form(data, request, uuid, guest_email=None):
    if guest_email:
        guest_user = GuestUser().get_user(email=guest_email)
        order = Order()
        request.session['email'] = guest_user[0]['email']
        menus = Order.get_all_by_guest(
            guest_user_id=guest_user[0]['id'])
        order.register_order(guest=guest_user[0]['id'],
                             data=data, uuid=uuid, list_menu=menus)
        return {'first_name': guest_user[0]['first_name']}
    else:
        guest = GuestUser().create_guest_user(data=data)
        order = Order()
        request.session['email'] = guest[0]['email']
        menus = order.get_all_by_guest(guest_user_id=guest[0]['id'])
        order.register_order(guest=guest[0]['id'],
                             data=data, uuid=uuid, list_menu=menus)
        return {'first_name': guest[0]['first_name']}
