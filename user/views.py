from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth import authenticate, login, logout, get_user_model

from user.mail_services import send_account_verification_email, send_password_reset_email
from .tokens import account_activation_token


User = get_user_model()


def signIn(request):
    if request.user.is_authenticated:
        return redirect(reverse("products"))
    if request.method == "POST":
        username = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next = request.session.get("next")
            print("next: ", next)
            if next:
                del request.session["next"]
                return redirect(next)
            return redirect(reverse("products"))
        else:
            messages.add_message(request, messages.ERROR, "invalid email of password")
            return render(request, template_name="user/signIn.html")
    else:
        next = request.GET.get("next")
        print("next: ", next)
        if next:
            request.session["next"] = next
        return render(request, template_name="user/signIn.html")


def register(request):
    if request.user.is_authenticated:
        return redirect(reverse("products"))
    error = False

    if request.method == "POST":
        first_name = request.POST["first_name"] or None
        last_name = request.POST["last_name"] or None
        email = request.POST["email"] or None
        mobile_number = request.POST["phone"] or None
        gender = request.POST["gender"] or None
        password = request.POST["password"] or None

        if first_name == None:
            messages.add_message(request, messages.ERROR, "First name is required")
            error = True
        if last_name == None:
            messages.add_message(request, messages.ERROR, "Last name is required")
            error = True
        if email == None:
            messages.add_message(request, messages.ERROR, "Email is required")
            error = True
        if mobile_number == None:
            messages.add_message(request, messages.ERROR, "Phone Number is required")
            error = True
        if password == None:
            messages.add_message(request, messages.ERROR, "Password must be provided")
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
            messages.add_message(
                request,
                messages.SUCCESS,
                "User created Successfully. Your can now log into your account",
            )
            send_account_verification_email(request, new_user)

            return redirect('not_verified_page')
            # return render(request, "user/signIn.html")

        except:
            messages.add_message(request, messages.ERROR, "User registration failed")
            return render(request, template_name="user/signUp.html")

    return render(request, template_name="user/signUp.html")

def not_verified(request):
    return render(request, 'user/not_activated.html')


def forget_password(request):
    if request.method == "POST":
        email = request.POST.get("email", None)
        if email is not None:
            User = get_user_model()
            try:
                usr = User.objects.get(email=email)
                send_password_reset_email(request, usr)
                return render(request, "user/email_reset_code_sent.html")

            except User.DoesNotExist:
                messages.add_message(
                    request, messages.ERROR, "No user with given email is found"
                )
        messages.add_message(
            request, messages.WARNING, "Please provide Your email address"
        )
    return render(request, "user/reset_password.html")


def new_password(request, id, token):
    # get user by verifying given id and token
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(id))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        # if user is found,
        if request.method == "GET":
            # if the request is get, meaning from the email, render set new password form
            return render(
                request,
                "user/set_new_password.html",
                context={"id": id, "token": token},
            )

        # if request is post, meaning from set password form,
        if request.method == "POST":
            password = request.POST.get("password", None)
            # check if password is provided
            if password is not None:
                try:
                    # try setting a new password for the user and then redirect to profile page
                    user.set_password(password)
                    user.save()
                    messages.add_message(
                        request,
                        messages.SUCCESS,
                        "Your password has been updated, you can now login with your new password.",
                    )
                    return render(request, "user/signin.html")
                except:
                    # if setting password failed, set an error message and redirect to set password page
                    messages.add_message(
                        request,
                        messages.ERROR,
                        "Unable to update your password, please try again",
                    )
                    return render(
                        request,
                        "user/set_new_password.html",
                        context={"id": id, "token": token},
                    )
            else:
                # if not password is provided from the form, set error and redirect back to set password page
                messages.add_message(
                    request, messages.ERROR, "Please prvide a valide password"
                )
                return render(
                    request,
                    "user/set_new_password.html",
                    context={"id": id, "token": token},
                )
    else:
        # if the id and/or token provided are wrong, redirect to invali_code page.
        return render(request, "user/invalid_code.html")


@login_required
def profile(request):
    return render(request, "user/profile.html")


@login_required
def editProfile(request):
    if request.method == "POST":
        first_name = request.POST["first_name"] or None
        last_name = request.POST["last_name"] or None
        mobile_number = request.POST["phone"] or None
        address = request.POST["address"] or None
        gender = request.POST["gender"] or None

        error = None

        if first_name == None:
            messages.add_message(request, messages.ERROR, "First name is required")
            error = True
        if last_name == None:
            messages.add_message(request, messages.ERROR, "Last name is required")
            error = True

        if mobile_number == None:
            messages.add_message(request, messages.ERROR, "Phone Number is required")
            error = True

        if address == None:
            messages.add_message(request, messages.ERROR, "Address is required")
            error = True

        if error:
            return render(request, "user/edit_profile.html")

        try:
            user = request.user
            user.first_name = first_name
            user.last_name = last_name
            user.mobile_number = mobile_number
            user.address = address
            user.gender = gender

            user.save()
            messages.add_message(request, messages.SUCCESS, "Profile updated")
            return render(request, "user/profile.html")
        except:
            messages.add_message(request, messages.ERROR, "Unable to update Profile")
            return render(request, template_name="user/edit_profile.html")

    return render(request, "user/edit_profile.html")


@login_required
def signout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("/")


def verify_account(request, id, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(id))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        login(request, user)
        messages.add_message(request, messages.SUCCESS, "Your account is now activated")
        return render(request, "/")
    else:
        return render(request, "accounts/invalid_code.html")
