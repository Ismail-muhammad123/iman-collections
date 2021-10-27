from django.http.response import Http404
from django.shortcuts import redirect, render, get_object_or_404
from .models import Product, Category
from django.contrib.auth.decorators import login_required
from django.db.models import Q


# Create your views here.


def home(request):

    categories = Category.objects.all()

    male = {
        "gender": "Male",
        "classes": categories.filter(gender="M")
    }
    female = {
        "gender": "Female",
        "classes": categories.filter(gender="F")
    }
    unisex = {
        "gender": "Unisex",
        "classes": categories.filter(gender="U")
    }

    context = {
        "categories": []
    }

    if len(unisex) > 0:
        context['categories'].append(unisex)
    if len(male) > 0:
        context['categories'].append(male)
    if len(female) > 0:
        context['categories'].append(female)

    return render(request, template_name="home/index.html", context=context)


def gender(request, gender):

    if gender.lower() == "male":
        g = "M"
    elif gender.lower() == "female":
        g = "F"
    elif gender.lower() == "unisex":
        g = "U"

    categories = Category.objects.filter(gender=g)

    context = {
        "categories": categories
    }

    return render(request, template_name="home/index.html", context=context)


def category_gender(request, gender, category):

    if gender.lower() == "male":
        g = "M"
    elif gender.lower() == "female":
        g = "F"
    elif gender.lower() == "unisex":
        g = "U"

    cat = get_object_or_404(Category, name=category, gender=g)

    products = Product.objects.filter(
        product_category=cat, available_quantity__gte=0)

    context = {
        "products": products,
        "category": cat,
        "gender": gender
    }

    return render(request, template_name="products/category_products.html", context=context)


def product_detaiil(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404(
            'The product with the given id could not be found'
        )

    print(product.image.url)
    context = {
        "size": product.size,
        "id": product.id,
        "name": product.name,
        "price": product.price,
        "available_quantity": product.available_quantity,
        "quantity_sold": product.quantity_sold,
        "brand": product.brand_name,
        "image": product.image.url,
        "delivery_days": product.delivery_in,
        "color": product.color

    }
    return render(request, template_name='products/product_detail.html', context=context)


def not_found(request):
    return render(request, template_name='home/not_found.html')


@login_required
def saved(request):
    return render(request, template_name="products/saved.html")


def error_404(request, exception):
    return render(request, 'home/404.html')


def error_500(request):
    return render(request, '500.html')
