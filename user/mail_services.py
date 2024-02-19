from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from .tokens import account_activation_token


def send_account_verification_email(request, user):
    current_site = get_current_site(request)
    mail_subject = "Tutornet Account activation link"
    message = render_to_string(
        "accounts/activation_email.html",
        {
            "user": user,
            "domain": current_site.domain,
            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            "token": account_activation_token.make_token(user),
        },
    )
    to_email = user.email
    email = EmailMessage(mail_subject, message, to=[to_email])
    email.send()


def send_password_reset_email(request, user):
    current_site = get_current_site(request)
    mail_subject = "Tutornet Password Reset link"
    message = render_to_string(
        "accounts/password_reset_email.html",
        {
            "user": user,
            "domain": current_site.domain,
            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            "token": account_activation_token.make_token(user),
        },
    )
    to_email = user.email
    email = EmailMessage(mail_subject, message, to=[to_email])
    email.send()
