# Django.
from Orders.utils import order_user_form
from Menus.models import Menu
from Orders.forms import OrderRegisterForm, OrderRegisterWithUser
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

    if request.method == 'POST':

        if request.session['email'] is not None:
            form = OrderRegisterForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                guest_user = order_user_form(
                    data=data, request=request, uuid=uuid)
                return render(request, 'orders/successful.html', context={'user': guest_user['first_name']})
            else:
                form = OrderRegisterForm()
        else:
            form = OrderRegisterWithUser(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                guest_user = order_user_form(
                    data=data, request=request, uuid=uuid)
                return render(request, 'orders/successful.html', context={'user': guest_user['first_name']})
            else:
                form = OrderRegisterWithUser()

    return render(request, 'orders/successful.html')
