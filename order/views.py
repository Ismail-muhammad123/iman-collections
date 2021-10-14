from django.shortcuts import render

# Create your views here.


def order(request):
    context = {
        "order_items": range(3),
    }
    return render(request, template_name='order/order.html', context=context)
