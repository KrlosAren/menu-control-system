# Django
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required


# Forms.
from .forms import GuestForm, SignupForm


@login_required(login_url='login_view')
def admin_home(request):

    context = {}

    return render(request, 'admin-home/index.html', context=context)


def login_view(request):
    """Login view."""

    context = {
        'title': 'Login User'
    }

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('admin_home')
        else:
            context['error'] = 'Invalid username and password'
            return render(request, 'users/login.html', context)

    return render(request, 'users/login.html', context=context)


def register_view(request):
    form = SignupForm()
    context = {
        'title': 'Register',
        'form': form
    }

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_view')

    return render(request, 'users/register.html', context=context)


@login_required(login_url='login_view')
def logout_view(request):
    """Logout a user."""
    logout(request)
    return redirect('login_view')


def guest_login(request):

    context = {
        'title': 'Order Form'
    }

    if request.method == 'POST':
        form = GuestForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            email = data['email']
            name = data['first_name']
        else:
            form = GuestForm()

    return render(request)
