# Django.
from django.contrib.auth import authenticate
from django.http import request
from Orders.forms import OrderRegisterForm
from Users.forms import GuestForm
from django.shortcuts import redirect, render

# Models
from .models import GuestUser

# Forms


# def order_register(request, uuid):
def order_register(request):

    form = OrderRegisterForm()

    context = {
        'title': 'Register Order',
        'form': form
    }
    # data = is_menu(uuid)

    if 'email' in request.session:

        email = request.session['email']

        is_guest_user = GuestUser.objects.filter(email=email).exists()
        if is_guest_user:
            guest_user = authenticate(email=email)
            context['guest_name'] = guest_user['first_name']
            return render(request, 'orders/order_register.html', context=context)
        else:
            order_form = OrderRegisterForm()
            context['order_form'] = order_form
            return render(request, 'orders/order_register.html', context=context)
    else:
        order_form = OrderRegisterForm()
        guest_form = GuestForm()
        context['guest_form'] = guest_form
        context['order_form'] = order_form
        return render(request, 'orders/order_register.html', context=context)


def order_save(request):

    context = {
        'title': 'Successfully'
    }

    if request.method == 'POST':

        guest_form = GuestForm(request.POST)
        order_form = OrderRegisterForm(request.POST)
        if guest_form.is_valid():
            data = guest_form.cleaned_data
            email = data['email']
            first_name = data['first_name']

    return render(request, 'order/successfully.html', context=context)
