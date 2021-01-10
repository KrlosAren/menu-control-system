# Django.
from Menus.models import Menu
from Orders.forms import OrderRegisterForm
from django.shortcuts import redirect, render


# Models
from .models import GuestUser, Order


def order_register(request, uuid):

    form = OrderRegisterForm()
    menu = Menu().filter_menu(uuid=uuid)

    context = {
        'title': 'Register Order',
        'form': form,
        'uuid': uuid,
        'menu': menu,
    }
    if request.session.get('email') is not None:
        guest_user = GuestUser().get_user(request.session.get('email'))
        context['user'] = guest_user[0]['first_name']
        return render(request, 'orders/order_register.html', context=context)
    else:
        context['user'] = None
        return render(request, 'orders/order_register.html', context=context)


def order_save(request, uuid):

    context = {
        'form': OrderRegisterForm()
    }

    if request.method == 'POST':

        form = OrderRegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            email = data['email']
            guest_user = GuestUser.get_user(email=email)
            if guest_user:
                order = Order()
                menus = Order.get_all(guest_user_id=guest_user[0]['id'])
                request.session['email'] = data['email']
                order.register_order(guest=guest_user[0]['id'],
                                     data=data, uuid=uuid, list_menu=menus)
            else:
                guest = GuestUser()
                order = Order()
                guest_id = guest.create_guest_user(data=data)[0]['id']
                menus = order.get_all(guest_user_id=guest_id)
                order.register_order(guest=guest_id,
                                     data=data, uuid=uuid, list_menu=menus)
        else:
            form = OrderRegisterForm()
    return render(request, 'orders/successful.html', context=context)
