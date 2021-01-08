# Django.
from Users.forms import GuestForm
from django.shortcuts import redirect, render

# Models
from .models import GuestUser

# Forms


def order_register(request, uuid):

    form = order_form()

    context = {
        'title': 'Register Order',
        'form': form
    }
    # data = is_menu(uuid)

    if 'email' in request.session:

        guest_user = GuestUser.objects.filter(email=request.session['email'])
        if guest_user:
            context['guest_name'] = guest_user['first_name']
            return render(request, 'order/register_order.html', context=context)
        else:
            return render(request, 'order/register_order.html', context=context)

    if request.method == 'POST':
        form = GuestForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            email = data['email']
            first_name = data['first_name']

    return render(request, 'order/order_register.html', context=context)


def order_post(request):

    if request.method == 'POST':
        import pdb
        pdb.set_trace()
        # is_email = request.session['email']
        # is_email = email_exists(request.POST['email'])
        # customer_user = CustomerUser(is_email, request.POST)

        # if is_email[0]:
        # pass
        # customer_user.cookie_session_set(request=request)
        # customer_user.user_login()
        # customer_user.register_order(request.POST)

        # else:
        # customer_user.register_order(request.POST)
        # customer_user.user_login()
        # customer_user.cookie_session_set(request=request)
        # return HttpResponse('registrado')

    return HttpResponse('su pedido fue agendado')


def order_and_save_user(request):

    new_user = CustomerUser(request.POST['email'], request.POST)

    new_user.cookie_session_set(request)
    new_user.user_login()

    new_user.register_order(order=request)

    return HttpResponse('tu pedido ha sido enviado')
