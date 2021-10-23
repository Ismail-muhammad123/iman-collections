from django.shortcuts import render
from .models import Order
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def order(request):

    ordered_items = Order.objects.all().filter(customer=request.user)
    context = {
        "order_items": ordered_items,
    }
    return render(request, template_name='order/order.html', context=context)
