"""
      Utils form orders module
    """


from Orders.models import Order
from Users.models import GuestUser


def order_user_form(data, request, uuid):
    email = request.session['email'] if request.session['email'] else data['email']
    guest_user = GuestUser.get_user(email=email)
    if guest_user:
        order = Order()
        menus = Order.get_all_by_guest(
            guest_user_id=guest_user[0]['id'])
        order.register_order(guest=guest_user[0]['id'],
                             data=data, uuid=uuid, list_menu=menus)
    else:
        guest = GuestUser()
        order = Order()
        guest_id = guest.create_guest_user(data=data)[0]['id']
        menus = order.get_all_by_guest(guest_user_id=guest_id)
        order.register_order(guest=guest_id,
                             data=data, uuid=uuid, list_menu=menus)
    return {'email': guest_user[0]['email'], 'first_name': guest_user[0]['first_name']}
