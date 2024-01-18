from unicodedata import category
from django.contrib import messages
from django.shortcuts import render
from base.models import ContactMessage
from products.models import Cart, Product, Category


def index(request):
    products = Product.objects.all()[0:15]
    categories = Category.objects.all()[0:10]
    return render(request, 'base/index.html', context={"products": products, "categories": categories})


def contact(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact_message = ContactMessage(
            full_name=full_name, email=email, subject=subject, message=message)
        contact_message.save()

        messages.add_message(request, messages.SUCCESS,
                             "We have recieved your message, we will get back to you soon.")
        return render(request, 'base/index.html')
    else:
        messages.add_message(request, messages.ERROR,
                             "Sorry! There has been an error while recieving your message. please try again.")
        return render(request, 'base/index.html')


def error_404(request, e):
    data = {}
    return render(request, "base/404.html", data)


def error_500(request):
    data = {}
    return render(request, "base/500.html", data)
