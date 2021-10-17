from django.shortcuts import render

# Create your views here.


def login(request):
    return render(request, template_name='user/signIn.html')


def register(request):
    return render(request, template_name='user/signUp.html')


def reset_password(request):
    return render(request, template_name='user/reset_password.html')
