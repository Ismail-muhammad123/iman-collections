import datetime
from multiprocessing import context
from django.shortcuts import render, redirect
from pytz import country_names
from products.models import Product
from django.shortcuts import get_object_or_404
from .models import Order, OrderItem
from django.http import Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


@login_required
def new_order(request):
    cart_items = request.user.cart.all()
    sub_total = 0
    for item in cart_items:
        sub_total += item.product.price * item.quantity

    # countries = [i[1] for i in country_names.items()]

    # countries.sort(reverse=True)

    countries = ['Nigeria']

    tax = 0

    delivery_fee = 0

    total = sub_total + tax + delivery_fee

    context = {
        "cart_items": cart_items,
        "sub_total": sub_total,
        "tax": tax,
        "countries": countries,
        "delivery_fee": delivery_fee,
        "total": total

    }
    return render(request, template_name='order/new_order.html', context=context)


def add_order(request):

    delivery_address = request.POST.get('delivery_address')
    country = request.POST.get('country')
    state = request.POST.get('state')
    zip_code = request.POST.get('zip_code')

    if (delivery_address == None or country == None or state == None):
        messages.add_message(request, messages.ERROR,
                             "All required fields must be provided")
        return new_order(request)

    cart_items = request.user.cart.all()

    total_amount = 0

    for item in cart_items:
        total_amount += item.product.price * item.quantity

    order = Order(
        country=country,
        state=state,
        zip_code=zip_code,
        delivery_address=delivery_address,
        total_amount=total_amount,
        user=request.user,
    )

    order.save()

    for item in cart_items:
        order_item = OrderItem(
            product=item.product,
            quantity=item.quantity,
            order=order
        )

        order_item.save()

    return redirect(reverse("order_checkout", kwargs={"order_id": order.id}))


def track_order(request):
    orders = request.user.orders.all()

    context = {"orders": orders}

    return render(request, "order/order.html", context=context)
