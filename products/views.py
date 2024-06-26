import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from products.serializers import ProductVariantSerializer
from .models import Cart, Category, Product, ProductVariant
from django.shortcuts import get_object_or_404
from django.db.models import Q  # new
from django.contrib.postgres.search import SearchVector
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime
from rest_framework.response import Response


def categories(request):
    categories = Category.objects.all()
    return render(
        request, "products/categories.html", context={"categories": categories}
    )


def products(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(
        request,
        template_name="products/products.html",
        context={"products": products, "categories": categories},
    )


def variants_json(request):
    variants = ProductVariant.objects.all()
    serializer = ProductVariantSerializer(instance=variants, many=True)
    return HttpResponse(json.dumps(serializer.data))


def product_category(request, slug):
    categories = Category.objects.all()
    if slug == "all":
        products = Product.objects.all()
    elif slug == "new":
        d = datetime.datetime.today() - datetime.timedelta(days=30)
        products = Product.objects.all().filter(added_at__gt=d)
    elif slug == "trending":
        products = Product.objects.all()
        products = [product for product in products if product.orders.count() >= 10]
    elif slug == "sale":
        products = Product.objects.filter(on_sale=True)
    else:
        category = get_object_or_404(Category, slug=slug)
        products = Product.objects.all().filter(category=category)

    context = {
        "products": products,
        "category_name": "All Categories"
        if slug == "all"
        else str.join(" ", str.split(slug, "-")),
        "categories": categories,
    }
    return render(request, template_name="products/products.html", context=context)


def product_details(request, slug, id):
    product = get_object_or_404(Product, id=id, slug=slug)

    context = {
        "product": product,
    }
    return render(
        request, template_name="products/product_detail.html", context=context
    )


def search(request):
    if request.method == "GET":
        data = request.GET

        search_term = data.get("search_term", "")

        if search_term == "":
            return redirect("products")

        products = (
            Product.objects.filter(
                Q(name__icontains=search_term)
                | Q(description__icontains=search_term)
                | Q(category__name__icontains=search_term)
            )
            if settings.DEBUG
            else Product.objects.annotate(
                search=SearchVector(
                    "name", "category__name", "brand_name", "description"
                ),
            ).filter(search=search_term)
        )

        categories = Category.objects.all()

        print(products)

        context = {
            "products": products,
            "category_name": f"Search result for '{search_term}'",
            "categories": categories,
        }

        return render(request, "products/products.html", context=context)


def cart(request):
    if request.user.is_authenticated:
        cart_items = request.user.cart.all()
    else:
        device = request.COOKIES["device"]
        cart_items = Cart.objects.filter(device=device)
    return render(request, "products/cart.html", context={"shoping_cart": cart_items})


def add_to_cart(request):
    data = request.GET
    variant_id = data.get("product_variant_id")
    quantity = data.get("quantity")

    variant = get_object_or_404(ProductVariant, id=variant_id)

    if request.user.is_authenticated:
        if len(request.user.cart.filter(product_variant=variant)) == 0:
            cart = Cart(product_variant=variant, quantity=quantity, user=request.user)
            cart.save()
    else:
        device = request.COOKIES["device"]
        if len(Cart.objects.filter(product_variant=variant, device=device)) == 0:
            cart = Cart(product_variant=variant, quantity=quantity, device=device)
            cart.save()
    return redirect(reverse("shoping_cart"))


def update_cart(request):
    cart_id = request.POST.get("cart_id")
    quantity = request.POST.get("quantity")

    cart = get_object_or_404(Cart, id=cart_id)

    cart.quantity = quantity

    cart.save()
    # messages.add_message(request, messages.SUCCESS,
    #                      "Cart Updated")
    return redirect(reverse("shoping_cart"))


def delete_cart(request, id):
    cart = get_object_or_404(Cart, id=id)
    cart.delete()
    return redirect(reverse("shoping_cart"))
