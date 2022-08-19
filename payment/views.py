from django.shortcuts import render

# Create your views here.


def checkout(request):
    items = range(5)

    return render(request, template_name='payment/checkout.html', context={"items": items})
