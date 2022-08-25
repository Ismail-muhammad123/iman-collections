import datetime
import imp
from django.shortcuts import render, redirect
from products.models import Product
from django.shortcuts import get_object_or_404
from .models import Order
from django.http import Http404


# Create your views here.


def new_order(request):
    if request.method == "GET":
        return redirect("/")

    if request.method == "POST":
        data = request.POST

        id = data.get('product_id', None)
        quantity = data.get('quantity', None)

        if id is None or quantity is None:
            return redirect('/')

        quantity = eval(quantity)

        try:
            product = Product.objects.get(id=id)
        except Product.DoesNotExist:
            raise Http404

        order = Order(
            product=product,
            quantity=quantity,
            total_amount=product.price * quantity,
            delivery_date=datetime.date.today() +
            datetime.timedelta(
                days=product.delivery_days
            )
        )

        order.save()
        return render(request, template_name='checkout/checkout.html', context={"order": order})


def my_order(request):
    return render(request, template_name='order/order.html')


def track_order(request, tracking_id):
    id = eval(tracking_id)
    order = get_object_or_404(Order, id)
    delivery_date = order.payment.payed_at + \
        datetime.timedelta(days=order.product.delivery_days)

    return render(request, template_name='order/order.html', cosntext={"order": order, "delivery_date": delivery_date})
