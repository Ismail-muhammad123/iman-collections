from django.db.models.base import ModelStateFieldsCacheDescriptor
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.conf import settings
from user.models import Account


# Create your views here.


def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/products')
        else:
            messages.error(request, 'Invalid Username or password')
            return render(request, template_name='user/signUp.html')
    else:
        if request.user.is_authenticated:
            messages.info(request, 'Your are already login in.')
            return redirect('/products')
        return render(request, template_name='user/signIn.html')


def register(request):
    if request.method == 'POST':
        data = request.POST

        if data['password2'] != data['password1']:
            messages.error(
                request, 'The two passwords provided are not identical')
            return redirect('/user/register')

        name = data['name']
        email = data['email']
        phone_number = data['phone_number']
        password = data['password1']

        user = Account.objects.create_user(
            name=name,
            email=email,
            phone_number=phone_number,
            password=password
        )

        login(request, user)
        messages.info(request, 'Account Created Successfully')
        return redirect('/products')
    if request.user.is_authenticated:
        messages.info(
            request, 'You are already signed into another account. logout and try again.')
        return redirect('/products')
    return render(request, template_name='user/signUp.html')


def reset_password(request):
    # TODO set up reset email funstionality
    return render(request, template_name='user/reset_password.html')


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, "Your are now Loged out of your account")
    return redirect('/user/login')
