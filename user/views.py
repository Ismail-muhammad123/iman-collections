from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your views here.


User = get_user_model()


def signIn(request):
    if request.method == "POST":
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('products'))
        else:
            messages.add_message(request, messages.ERROR,
                                 "invalid email of password")
            return render(request, template_name='user/signIn.html')
    else:
        return render(request, template_name='user/signIn.html')


def register(request):

    error = False

    if request.method == "POST":
        first_name = request.POST["first_name"] or None
        last_name = request.POST["last_name"] or None
        email = request.POST["email"] or None
        mobile_number = request.POST["phone"] or None
        gender = request.POST["gender"] or None
        password = request.POST["password"] or None

        if first_name == None:
            messages.add_message(request, messages.ERROR,
                                 "First name is required")
            error = True
        if last_name == None:
            messages.add_message(request, messages.ERROR,
                                 "Last name is required")
            error = True
        if email == None:
            messages.add_message(request, messages.ERROR,
                                 "Email is required")
            error = True
        if mobile_number == None:
            messages.add_message(request, messages.ERROR,
                                 "Phone Number is required")
            error = True
        if password == None:
            messages.add_message(request, messages.ERROR,
                                 "Password must be provided")
            error = True

        if error:
            return render(request, "user/signUp.html")

        try:
            new_user = User.objects.create_user(email=email, password=password)

            new_user.first_name = first_name
            new_user.last_name = last_name
            new_user.mobile_number = mobile_number
            new_user.gender = gender

            new_user.save()
            messages.add_message(request, messages.SUCCESS,
                                 "User created Successfully. Your can now log into your account")
            return render(request, "user/signIn.html")

        except:
            messages.add_message(request, messages.ERROR,
                                 "User registration failed")
            return render(request, template_name='user/signUp.html')

    return render(request, template_name='user/signUp.html')


def profile(request):
    pass


def reset_password(request):
    return render(request, template_name='user/reset_password.html')


def signout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("/")
