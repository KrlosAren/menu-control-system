# Django
import pdb
from django.contrib.messages.api import debug, get_messages
from django.core.checks.messages import Error
from django.db.models.query import prefetch_related_objects
from django.forms.utils import ErrorList
from django.http.response import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError

# forms
from Menus.forms import MenuRegister, MenuUpdate

# Menu Model
from .models import Menu

# tasks
from .tasks import slack_msg

# celery
from celery.result import AsyncResult


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
        if form.is_valid():
            data = form.cleaned_data
            try:
                Menu().menu_register(data=data, admin_user=request.user)
                return redirect('menu_list_view')
            except IntegrityError as e:
                context['error'] = 'Ya tienes un menu para ese dia.'
                return render(request, 'menus/menu_register.html', context=context)
        else:
            form = MenuRegister()

    return render(request, 'menus/menu_register.html', context=context)


@login_required(login_url='login_view')
def menu_update(request, uuid):
    menu = Menu().filter_menu(uuid=uuid)

    context = {
        'title': 'Update Menu',
        'menu': menu.values()[0],
    }

    if request.method == 'POST':

        form = MenuUpdate(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            menu = Menu().update(data=data, uuid=uuid)

            return redirect('menu_list_view')

    return render(request, 'menus/menu_update.html', context=context)


@login_required(login_url='login_view')
def menu_delete(request, uuid):

    if request.method == 'POST':
        menu = Menu().filter_menu(uuid=uuid)

        if menu:
            menu.delete()
        else:
            raise ValueError('Este menu no existe')

    return redirect('menu_list_view')


@login_required(login_url='login_view')
def menu_list(request):

    menus = Menu().all_menus(admin_user_id=request.user.id).order_by('date')

    context = {
        'title': 'Menu List',
        'menus': menus,
        'messages': get_messages(request)
    }
    return render(request, 'menus/menu_list.html', context=context)


@login_required(login_url='login_view')
def menu_send(request, uuid):

    if request.method == 'POST':
        menu = Menu().filter_menu(uuid=uuid)
        menu.send = True
        menu.save()
        response = slack_msg.delay(
            menu.uuid, request.META.get('HTTP_HOST'))

    return redirect('menu_list_view')
