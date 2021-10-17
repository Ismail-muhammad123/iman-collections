from django.shortcuts import render

# Create your views here.


def products(request):
    context = {
        "products": range(8),
        "categories": ['shirts', 'trousers', 'caps', 'shoes']
    }
    return render(request, template_name="products/products.html", context=context)


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


def product_detaiil(request):
    context = {
        "product_sizes": ['sm', 'md', 'lg', 'xl'],
        "simialr_items": range(5),
    }
    return render(request, template_name='products/product_detail.html', context=context)


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
