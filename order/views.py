from django.contrib.auth import login
from django.shortcuts import render
from .models import Order, OrderProduct
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def order(request):

    orders = Order.objects.all().filter(customer=request.user)
    context = {
        "orders": orders,
    }
    return render(request, template_name='order/order.html', context=context)


@login_required
def order_detail(request, order_id):
    items = Order.objects.get(id=order_id).order_products.all()
    context = {
        "items": items
    }

    return render(request, template_name="order/details.html", context=context)
