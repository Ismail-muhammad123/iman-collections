from unicodedata import category
from django.shortcuts import render
from products.models import Product, Category



def index(request):
    products = Product.objects.all()[0:8]
    categories = Category.objects.all()
    return render(request, 'base/index.html', context={"products": products, "categories": categories})
