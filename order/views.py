from datetime import datetime, timedelta
from multiprocessing import context
from django.shortcuts import render, redirect
from pytz import country_names
from products.models import Cart, Product
from django.shortcuts import get_object_or_404
from .models import Order, OrderItem
from django.http import Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core import mail


def new_order(request):
    if request.user.is_authenticated:
        cart_items = request.user.cart.all()
        full_name = request.user.get_full_name()
        email = request.user.email
        phone_number = request.user.mobile_number
    else:
        full_name = ""
        email = ""
        phone_number = ""
        device = request.COOKIES["device"]
        cart_items = Cart.objects.filter(device=device)

    sub_total = 0
    delivery_fee = 0
    total = 0
    for item in cart_items:
        sub_total += item.product_variant.price * item.quantity
        delivery_fee += item.product_variant.delivery_fee * item.quantity

    # countries = [i[1] for i in country_names.items()]

    # countries.sort(reverse=True)

    countries = ["Nigeria"]
    total = sub_total + delivery_fee
    # tax = 7.5 * 0.01 * float(total)
    tax = 0

    context = {
        "cart_items": cart_items,
        "sub_total": sub_total,
        "tax": tax,
        "countries": countries,
        "delivery_fee": delivery_fee,
        "total": total,
        "full_name": full_name,
        "email": email,
        "phone_number": phone_number,
    }
    return render(request, template_name="order/new_order.html", context=context)


def add_order(request):
    delivery_address = request.POST.get("delivery_address")
    country = request.POST.get("country")
    state = request.POST.get("state")
    zip_code = request.POST.get("zip_code")

    full_name = request.POST.get("full_name")
    email = request.POST.get("email")
    phone_number = request.POST.get("phone_number")

    if delivery_address == None or country == None or state == None:
        messages.add_message(
            request, messages.ERROR, "All required fields must be provided"
        )
        return new_order(request)

    if request.user.is_authenticated:
        cart_items = request.user.cart.all()
    else:
        cart_items = Cart.objects.filter(device=request.COOKIES["device"])

    # cart_items = request.user.cart.all() if request.user.is_autheticated else Cart.objects.filter(
    #     device=request.COOKIES['device'])

    if len(cart_items) == 0:
        raise Http404()

    sub_total = 0
    total_delivery_fee = 0
    tax = 0

    order = Order(
        full_name=full_name,
        email=email,
        phone_number=phone_number,
        country=country,
        state=state,
        zip_code=zip_code,
        delivery_address=delivery_address,
        user=request.user,
    )
    order.save()

    for item in cart_items:
        sub_total += item.product_variant.price * item.quantity
        total_delivery_fee += item.product_variant.delivery_fee

        if request.user.is_authenticated:
            order.user = request.user
        else:
            order.device = request.COOKIES["device"]

        # for item in cart_items:
        order_item = OrderItem(
            product=item.product_variant,
            quantity=item.quantity,
            order=order,
            seller=item.product.store,
            tax=0,
            delivery_fee=item.product.delivery_fee,
            delivery_status=1,
            delivery_date=datetime.today()
            + timedelta(days=item.product.product.delivery_days),
        )

        order_item.save()
    return redirect(reverse("order_checkout", kwargs={"order_id": order.id}))


def track_order(request):
    if request.user.is_authenticated:
        orders = request.user.orders.exclude(status=4)
    else:
        orders = Order.objects.filter(device=request.COOKIES["device"]).exclude(
            status=4
        )

    context = {"orders": orders}

    return render(request, "order/order.html", context=context)

