# Django
from Orders.models import Order
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required


# Forms.
from .forms import SignupForm


@login_required(login_url='login_view')
def admin_home(request):

    context = {}

    orders = Order()

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
        import pdb; pdb.set_trace()
        if user:
            login(request, user)
            return redirect('admin_home')
        else:
            context['error'] = 'Invalid username and password'
            return render(request, 'users/login.html', context)

    return render(request, 'users/login.html', context=context)


def register_view(request):

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login_view')
    else:
        form = SignupForm()

    return render(request, 'users/register.html', context={
        'form': form,
        'title': 'Register',
    })


@login_required(login_url='login_view')
def logout_view(request):
    """Logout a user."""
    logout(request)
    return redirect('login_view')


