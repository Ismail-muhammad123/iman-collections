from products.models import Cart


def get_cart_count(request):
    return {
        "cart_count": request.user.cart.count() if request.user.is_authenticated else Cart.objects.filter(
            device=request.COOKIES.get('device')).count() or '0'
    }
