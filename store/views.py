from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


from products.models import Category
from .models import Store


@login_required
def create_store(request):
    if request.method == "POST":
        data = request.data
        store = Store.objects.create(
            business_name=data["business_name"],
            business_address=data["business_address"],
            email=data["email"],
            altername_email=data["altername_email"],
            phone_number=data["phone_number"],
            alternate_phone_number=data["alternate_phone_number"],
            about=data["about"],
            is_registered=data["is_registered"],
            tin=data["tin"],
            rc_number=data["rc_number"],
            bank_name=data["bank_name"],
            account_name=data["account_name"],
            account_number=data["account_number"],
            bvn=data["bvn"],
        )
        store.owner = request.user
        store.save()

        usr = request.user
        usr.staff = True
        usr.is_seller = True
        usr.save()
        
        return render(request, "store/checkout.html")
    return render(request, "store/create_store.html")


def get_store_verification_status(request):
    pass


def close_store(request):
    pass


# PRODUCTS
def store_products(request, store_id):
    category_id = request.GET.get("category", None)
    store = get_object_or_404(Store, id=store_id)
    category_name = None
    if category_id is not None:
        category = Category.objects.get(id=category_id)
        category_name = category.name
        products = store.products.filter(category=category)
    else:
        products = store.products.all()

    return render(
        request,
        "store/store_products.html",
        context={
            "products": products,
            "categories": Category.objects.all(),
            "store": store,
            "category_name": category_name,
        },
    )


def remove_product(request):
    pass
