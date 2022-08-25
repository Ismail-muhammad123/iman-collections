import datetime
from django.shortcuts import render, redirect
from products.models import Product
from django.shortcuts import get_object_or_404
from .models import Order
from django.http import Http404
from django.urls import reverse


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
    order_id = request.GET.get("order_id", None)

    if order_id is not None:
        return redirect(reverse('track_order', args=[order_id]))
    else:
        return render(request, template_name='order/order.html')


def track_order(request, tracking_id):
    id = eval(tracking_id)
    try:
        order = Order.objects.get(id=id)
        delivery_date = order.payment.payed_at + \
            datetime.timedelta(days=order.product.delivery_days)

        return render(request, template_name='order/order.html', context={"order": order, "delivery_date": delivery_date})
    except:
        raise Http404
