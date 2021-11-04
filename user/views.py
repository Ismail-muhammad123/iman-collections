from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.conf import settings
from user.models import Account
from django.contrib.auth.hashers import check_password


from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = Account.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "user/password_reset_mail_sent.html"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Fashiona',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@example.com',
                                  [user.email], fail_silently=False)
                    except BadHeaderError:

                        return HttpResponse('Invalid header found.')

                    messages.success(
                        request, 'A message with reset password instructions has been sent to your inbox.')
                    return redirect("login")
            messages.error(request, 'An invalid email has been entered.')
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="user/password_reset.html", context={"password_reset_form": password_reset_form})


# Create your views here.


def user_login(request):

    if request.method == "POST":
        next = request.POST.get('next', None)
        username = request.POST['username'].strip()
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if next is not None:
                return redirect(next)
            return redirect('/products')
        else:
            messages.error(request, 'Invalid Username or password')
            if next is not None:
                context = {
                    "next": next
                }
                return render(request, template_name='user/signIn.html', context=context)

            return render(request, template_name='user/signIn.html')
    else:
        next = request.GET.get('next', None)
        if request.user.is_authenticated:
            messages.info(request, 'Your are already login in.')
            return redirect('/products')
        if next is not None:
            context = {
                "next": next
            }
            return render(request, template_name='user/signIn.html', context=context)
        return render(request, template_name='user/signIn.html')


def register(request):
    if request.method == 'POST':
        data = request.POST
        next = data.get('next', None)

        if data['password2'] != data['password1']:
            messages.error(
                request, 'The two passwords provided are not identical')

            if next is not None:
                context = {
                    "next": next
                }
                return render(request, template_name='user/signUp.html', context=context)

            return render(request, template_name='user/signUp.html')

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
        if next is not None:
            return redirect(next)

        return redirect('/products')
    if request.user.is_authenticated:
        messages.info(
            request, 'You are already signed into another account. logout and try again.')
        return redirect('/products')

    next = request.GET.get('next', None)
    if next is not None:
        context = {
            "next": next
        }
        return render(request, template_name='user/signUp.html', context=context)

    return render(request, template_name='user/signUp.html')


@login_required
def update_password(request):
    if request.method == "POST":
        data = request.POST
        user_password = data['current_password']
        password1 = data['p1']
        password2 = data['p2']

        if password1 != password2:
            messages.error(request, 'Both passwords must match')
            return render(request, 'user/change_password.html')

        user = request.user

        if check_password(user_password, user.password):
            user.set_password(password1)
            user.save()
            login(request, user)
            messages.success(request, 'Password Updated')
            return redirect('profile')
        else:
            messages.error(
                request, 'Your Current password does not match your password')
            return redirect('profile')

    return render(request, template_name='user/change_password.html')


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, "Your are now Loged out of your account")
    return redirect('/user/login')


@login_required
def profile(request):

    user = request.user
    if request.method == "POST":
        data = request.POST
        profile_image = request.FILES['profile_image']

        name = data['user_name']
        email = data['email']
        phone_number = data['phone_number']
        country = data['country']
        state = data['state']
        directions = data['directions']

        user.name = name
        user.email = email
        user.phone_number = phone_number
        user.country = country
        user.state = state
        user.directions = directions
        user.profile_picture = profile_image

        user.save()

        messages.success(request, 'Profile updated')
        return render(request, 'user/profile.html')

    return render(request, 'user/profile.html', {"user": user})


def reset_password(request):
    pass
