# Django
import pdb
from django.http.response import Http404, HttpResponse
from Menus.forms import MenuRegister
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Others

# Menu Model
from .models import Menu


@login_required(login_url='login_view')
def menu_register(request):
    import datetime

    form = MenuRegister()
    today = datetime.datetime.today()
    context = {
        'title': 'Menu Register',
        'form': form,
        'today': today
    }

    if request.method == 'POST':
        form = MenuRegister(request.POST)
        import pdb
        pdb.set_trace()
        if form.is_valid():
            data = form.cleaned_data

            date = data['date']
            option_1 = data['option_1']
            option_2 = data['option_2']
            option_3 = data['option_3']
            option_4 = data['option_4']
            admin_user = request.user

            menu = Menu()
            menu.date = date
            menu.option_1 = option_1
            menu.option_2 = option_2
            menu.option_3 = option_3
            menu.option_4 = option_4
            menu.admin_user = admin_user
            menu.save()
            if menu:
                return redirect('menu_list_view')
            else:
                context['errors'] = 'El menu ya ha sido creado'
                return render(request, 'menus/menu_register.html', context=context)
        else:
            form = MenuRegister()

    return render(request, 'menus/menu_register.html', context=context)


@login_required(login_url='login_view')
def menu_update(request, uuid):
    menu = Menu.objects.filter(uuid=uuid)

    context = {
        'title': 'Update Menu',
        'menu': menu.values()[0],
    }

    if request.method == 'POST':

        form = MenuRegister(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            menu = Menu.objects.get(uuid=uuid)
            menu.date = data['date']
            menu.option_1 = data['option_1']
            menu.option_2 = data['option_2']
            menu.option_3 = data['option_3']
            menu.option_4 = data['option_4']
            menu.save()

            return redirect('menu_list_view')

    return render(request, 'menus/menu_update.html', context=context)


@login_required(login_url='login_view')
def menu_delete(request, uuid):

    if request.method == 'POST':
        menu = Menu.objects.filter(uuid=uuid)

        if menu:
            menu.delete()
        else:
            raise ValueError('Este menu no existe')

    return redirect('menu_list_view')


@login_required(login_url='login_view')
def menu_list(request):

    menus = Menu.objects.all().filter(admin_user_id=request.user.id).order_by('date')

    context = {
        'title': 'Menu List',
        'menus': menus
    }
    return render(request, 'menus/menu_list.html', context=context)
