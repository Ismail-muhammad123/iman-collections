from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Cart, Category, Product
from django.shortcuts import get_object_or_404
from django.db.models import Q  # new
from django.contrib.postgres.search import SearchVector
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def categories(request):

    categories = Category.objects.all()

    return render(request, 'products/categories.html', context={"categories": categories})


def products(request):

    products = Product.objects.all()
    categories = Category.objects.all()

    return render(request, template_name="products/products.html", context={"products": products, "categories": categories})


def product_category(request, category_id):

    categories = Category.objects.all()

    if category_id == 'all':
        products = Product.objects.all()
    else:
        category = get_object_or_404(Category, id=category_id)
        products = Product.objects.all().filter(category=category)

    context = {
        "products": products,
        "category_name": "All Categories" if category_id == 'all' else category.name,
        "categories": categories,
    }
    return render(request, template_name="products/products.html", context=context)


def product_details(request, id):

    product = get_object_or_404(Product, id=id)

    context = {
        "product": product,
    }
    return render(request, template_name='products/product_detail.html', context=context)


def search(request):
    if request.method == "GET":
        data = request.GET

        search_term = data.get("search_term", "")

        if search_term == "":
            return redirect('products')

        products = Product.objects.filter(Q(name__icontains=search_term) | Q(description__icontains=search_term) | Q(category__name__icontains=search_term)) if settings.DEBUG else Product.objects.annotate(
            search=SearchVector('name', 'category__name',
                                'brand_name', 'description'),
        ).filter(search=search_term)

        categories = Category.objects.all()

        print(products)

        context = {
            "products": products,
            "category_name": f"Search result for '{search_term}'",
            "categories": categories,
        }

        return render(request, 'products/products.html', context=context)


@login_required
def cart(request):
    cart_items = request.user.cart.all()
    return render(request, "products/cart.html", context={"shoping_cart": cart_items})


@login_required
def add_to_cart(request):
    id = request.GET.get("product_id")
    quantity = request.GET.get("quantity")
    product = get_object_or_404(Product, id=id)

    if len(Cart.objects.filter(product=product)) == 0:
        cart = Cart(product=product, quantity=quantity, user=request.user)
        cart.save()
    # messages.add_message(request, messages.SUCCESS,
    #                      "Item added to your shoping cart")
    return redirect(reverse('shoping_cart'))


@login_required
def update_cart(request):
    cart_id = request.POST.get("cart_id")
    quantity = request.POST.get("quantity")

    cart = get_object_or_404(Cart, id=cart_id)

    cart.quantity = quantity

    cart.save()
    # messages.add_message(request, messages.SUCCESS,
    #                      "Cart Updated")
    return redirect(reverse("shoping_cart"))


@login_required
def delete_cart(request, id):
    cart = get_object_or_404(Cart, id=id)
    cart.delete()
    return redirect(reverse("shoping_cart"))
