from django.shortcuts import redirect, render
from .models import Cart
from products.models import Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def cart(request):
    if request.GET:
        item_id = request.GET['id']
        quantity = request.GET['quantity']
        size = request.GET['size']

        item = Product.objects.get(id=item_id)

        cart = Cart.objects.create(
            item=item,
            quantity=quantity,
            size=size,
            user=request.user
        )
        cart.save()

    price = 0.0

    cart_objects = Cart.objects.all().filter(user=request.user)

    for i in cart_objects:
        print('price: ', repr(i.item.price))
        price += i.item.price

    context = {
        'total_quantity': sum(cart_objects.values_list('quantity')[0]) if cart_objects else 0,
        'number_of_items': len(cart_objects),
        'total_price': price,
        "cart_items": cart_objects,
    }
    return render(request, template_name="cart/cart.html", context=context)

@login_required
def remove(request):
    id = request.GET['id']
    Cart.objects.get(id=id, user=request.user).delete()
    return redirect("/cart")

@login_required
def clear(request):
    items = Cart.objects.all().filter(user=request.user)
    items.delete()
    messages.info(request, 'Cart Items Removed.')
    return redirect('/cart')
