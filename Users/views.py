# Django
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required


# Forms.
from .forms import SignupForm


def home(request):

    context = {}

    return render(request, 'index.html', context=context)


def login_view(request):
    """Login view."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username and password'})

    return render(request, 'users/login.html')


def register_view(request):
    context = {
        'title': 'Register'
    }

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    return render(request, 'users/register.html', context=context)


@login_required
def logout_view(request):
    """Logout a user."""
    logout(request)
    return redirect('users:login')


def guest_login(request):

    if request.method == 'POST':
        