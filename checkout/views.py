from django.shortcuts import render, redirect
from django.conf import settings
import uuid
from django.shortcuts import get_object_or_404
from .models import Payment
from order.models import Order
import requests
from django.contrib import messages
from django.urls import reverse


def checkout(request):

    if request.method == "POST":
        params = request.POST

        order_id = params.get("order_id", None)
        if order_id is None:
            return redirect('/')

        unique_id = str(uuid.uuid4())

        order_id = eval(order_id)
        order = get_object_or_404(Order, id=order_id)

        f_name = params.get("first_name", None)
        l_name = params.get("last_name", "")
        email = params.get("email", None)
        phone = params.get("phone", None)
        address = params.get("address", None)
        country = params.get("country", None)
        state = params.get("state", None)
        postal_code = params.get("postal_code", None)

        try:
            payment = Payment(
                order=order,
                first_name=f_name,
                last_name=l_name,
                phone_number=phone,
                delivery_address=address,
                email=email,
                payment_referance_number=unique_id,
                amount=order.total_amount,
                country=country,
                postal_code=postal_code,
                state=state
            )
            payment.save()
        except:
            messages.add_message(
                request, messages.ERROR, "Error! Make sure all required field are proviede")
            return render(request, template_name='checkout/checkout.html', context={"order": order})

        url = settings.PAYMENT_GATEAWAY_URL
        secret_key = settings.PAYMENT_GATEAWAY_SECRET_KEY

        headers = {"Authorization": f"Bearer {secret_key}"}

        data = {
            "tx_ref": unique_id,
            "amount": order.total_amount,
            "currency": "NGN",
            "redirect_url": "https://fashiona-store.herokuapp.com/checout/verify",
            "meta": {
                "order_id": order.id,
            },
            "customer": {
                "email": email,
                "phonenumber": phone,
                "name": f"{f_name} {l_name}"
            },
            "customizations": {
                "title": "Iman Clothing and Apparels",
            }
        }

        print('redirect urls', reverse('verify_checkout'))

        res = requests.post(url, headers=headers, json=data)
        response = res.json()

        if response['status'] == "success":
            return redirect(response['data']['link'])
        else:
            messages.add_message(request, messages.ERROR, "Transaction failed")
            return render(request, template_name='checkout/checkout.html', context={"order": order})

    else:
        return redirect("/")


def verify_payment(request):
    pass
