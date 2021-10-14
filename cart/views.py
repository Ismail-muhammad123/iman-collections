from django.shortcuts import render

# Create your views here.


def cart(request):
    context = {
        "cart_items": range(4)
    }
    return render(request, template_name="cart/cart.html", context=context)
