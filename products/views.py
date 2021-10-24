from django.shortcuts import render
from .models import Product
from django.contrib.auth.decorators import login_required

# Create your views here.


def products(request):
    products = Product.objects.all()

    for i in products:
        i.image = i.image.url
        i.sizes = [j.strip() for j in i.sizes.split(',')]

    context = {
        "products": products,
    }
    return render(request, template_name="products/products.html", context=context)


def product_detaiil(request, id):
    product = Product.objects.get(id=id)
    print(product.image.url)
    sizes = product.sizes.split(',')
    context = {
        "product_sizes": sizes,
        "id" : product.id,
        "name" : product.name,
        "price" : product.price,
        "available_quantity" : product.available_quantity,
        "quantity_sold": product.quantity_sold,
        "brand": product.brand_name,
        "image" : product.image.url,
        "delivery_days": product.delivery_in,
        "color" : product.color

    }
    return render(request, template_name='products/product_detail.html', context=context)


def home(request):
    return render(request, template_name='home/index.html')


def category(request, cat):
    context = {
        "products": range(14),
        "categories": [cat]
    }
    return render(request, template_name="products/products.html", context=context)


def fabrics(request):
    return render(request, template_name='products/fabrics.html')


def not_found(request):
    return render(request, template_name='home/not_found.html')


def tailored(request):
    context = {
        "products": range(3),
        "categories": ['senator wares', 'kufta', 'jamfa', 'babbar riga']
    }
    return render(request, template_name='products/tailored.html', context=context)

@login_required
def saved(request):
    return render(request, template_name="products/saved.html")
