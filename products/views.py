from django.shortcuts import render

# Create your views here.


def products(request):
    context = {
        "products": range(4),
        "categories": ['shirts', 'trousers', 'caps', 'shoes']
    }
    return render(request, template_name="products/products.html", context=context)


def home(request):
    return render(request, template_name='home/index.html')
