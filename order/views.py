import imp
from django.shortcuts import render, redirect
from products.models import Product
from django.shortcuts import get_object_or_404
from .models import Order

# Create your views here.


def order(request):
    if request.method == "GET":
        return redirect("/")

    id = request.data['id']
    quantity = request.data['quantity']

    product = get_object_or_404(Product, id=id)

    amount = product.price*quantity

    order = Order(product=product, quantity=quantity, amount=amount)
    order.save()

    context = {
        "order": order,
    }
    return render(request, template_name='order/order.html', context=context)
