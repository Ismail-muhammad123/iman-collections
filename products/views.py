from django.http.response import Http404
from django.shortcuts import redirect, render, get_object_or_404
from .models import Product, Category, SavedProducts
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages


def search(request):
    # TODO create search functionality
    # product = Product.objects.filter()
    pass


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


def contact(request):
    if request.method == "GET":
        return render(request, 'home/contact.html')


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


@login_required
def saved(request):
    products = SavedProducts.objects.filter(user=request.user)

    return render(request, template_name="products/saved.html", context={"products": products})


@login_required
def save_item(request):
    id = request.GET['item_id']

    other_saved = SavedProducts.objects.filter(user=request.user, id=id)

    if not other_saved:
        product = Product.objects.get(id=id)

        s = SavedProducts.objects.create(user=request.user, item=product)
        s.save()

        messages.success(request, "Item Saved successfuly")
        return redirect('/products/detail/'+id)
    else:
        messages.info(request, "Item already saved")
        return redirect('/products/detail/' + id)


@login_required
def remove_saved(request):
    id = request.GET['id']

    s = SavedProducts.objects.get(user=request.user, id=int(id))
    s.delete()

    messages.info(request, "Item removed successfuly")
    return redirect('/products/saved', permanent=True)


def error_404(request, exception):
    return render(request, 'home/404.html')


def error_500(request):
    return render(request, '500.html')
