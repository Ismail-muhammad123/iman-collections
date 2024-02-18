from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from django.contrib import messages
from products.models import Category
from .models import Plan, Store, Subscription, SubscriptionPayment

# NEW ACCOUNT: create a store -> *choose a plan* -> *make payment* -> open profile and view verification status -> activate store -> open dashboard
# OLD ACCOUNT: view profile -> update plan -> make payment -> view admin page
# ADMIN: add product -> add variant -> publish product -> view oders -> update order and delivery status -> update/deactivate a product


def make_payment(subscription):
    pass


def verify_payment(request):
    pass


@login_required
def create_store(request):
    store, created = Store.objects.get_or_create(
        owner=request.user,
    )
    if request.method == "POST":
        data = request.POST
        if created:
            store.business_name = data["business_name"]
            store.business_address = data["business_address"]
            store.email = data["email"]
            store.alternate_email = data["alternate_email"]
            store.phone_number = data["phone_number"]
            store.alternate_phone_number = data["alternate_phone_number"]
            store.about = data["about"]
            # store.is_registered = data.get("registration_status", "0") == "1"
            # store.tin = data["tin"]
            # store.rc_number = data["rc_number"]
            store.bank_name = data["bank_name"]
            store.account_name = data["account_name"]
            store.account_number = data["account_number"]
            store.bvn = data["bvn"]

            store.save()

            # update user to seller
            usr = request.user
            usr.staff = True
            usr.is_seller = True
            usr.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Your Store has been created successfully",
            )
            # plans = Plan.objects.all()
            return render(request, "store/store_profile.html", context={"store": store})

        else:
            store.business_name = data["business_name"]
            store.business_address = data["business_address"]
            store.email = data["email"]
            store.alternate_email = data["alternate_email"]
            store.phone_number = data["phone_number"]
            store.alternate_phone_number = data["alternate_phone_number"]
            store.about = data["about"]
            # store.is_registered = data.get("registration_status", "0") == "1"
            # store.tin = data["tin"]
            # store.rc_number = data["rc_number"]
            store.save()

            messages.add_message(
                request,
                messages.SUCCESS,
                "Your Store has been Updated",
            )
            return render(request, "store/store_profile.html", context={"store": store})
    else:
        return render(request, "store/create_store.html", context={"store": store})


@login_required
def update_plan(request):
    plans = Plan.objects.all()
    store = request.user.store

    if request.method != "POST":
        current_plan = None
        if store is not None:
            current_plan = store.subscription.plan
        return render(
            request,
            "store/update_plan.html",
            context={"plans": plans, "current_plan": current_plan},
        )

    if store is not None:
        plan_id = request.POST.get("plan_id", None)
        frequency = int(request.POST.get("frequency", "1"))
        if plan_id is not None:
            plan = Plan.objects.get(id=plan_id)
            sub, created = Subscription.objects.get_or_create(store=store)
            sub.plan = plan
            sub.expires_at = datetime.now() + timedelta(days=30 * frequency)
            sub.status = 1
            sub.amount = plan.price * frequency
            sub.save()

            sub_payment = SubscriptionPayment.objects.create(
                subscription=sub,
                amount=sub.amount,
                store=store,
                status=2,
            )

            sub_payment.save()
            make_payment(subscription=sub)
        else:
            render(request, "store/select_plan.html", context={"plans": plans})
    else:
        return redirect("/")


@login_required
def view_store_profile(request):
    store = request.user.store
    if store is not None:
        return render(request, "store/store_profile.html", context={"store": store})
    else:
        if request.user.is_admin:
            return redirect("/admin")
        else:
            messages.add_message(
                request,
                messages.INFO,
                "You do not have a store yet, fill in the form below to get started",
            )
            return render(request, "store/create_store.html")


@login_required
def activate_store(request):
    pass


@login_required
def deactivate_store(request):
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
