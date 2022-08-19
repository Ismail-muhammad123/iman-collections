from django.shortcuts import render
from .models import Category, Product
from django.shortcuts import get_object_or_404


# Create your views here.


def categories(request):
    pass


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

    print(product)

    return render(request, template_name='products/product_detail.html', context=context)


def cart(request):

    items = range(3)

    return render(request, template_name="products/cart.html", context={"items": items})


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


def saved(request):
    return render(request, template_name="products/saved.html")
