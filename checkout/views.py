from datetime import datetime
from pprint import pprint
from django.shortcuts import render, redirect
from django.conf import settings
import uuid
from django.shortcuts import get_object_or_404
from .models import Payment
from order.models import Order
import requests
from django.contrib import messages
from django.urls import reverse
from django.http import Http404


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
            pprint(response)
            return redirect(response['data']['link'])
        else:
            messages.add_message(request, messages.ERROR, "Transaction failed")
            return render(request, template_name='checkout/checkout.html', context={"order": order})

    else:
        return redirect("/")


def verify_payment(request):
    headers = {"Authorization": f"Bearer {settings.PAYMENT_GATEAWAY_SECRET_KEY}"}
    data = request.GET

    tx_ref = data['tx_ref']
    response = requests.get("https://api.flutterwave.com/v3/transactions/verify_by_reference",
                            headers=headers, params={"tx_ref": tx_ref})
    if response.status_code == 200:
        res = response.json()
        status = res['status'] == "success"
        if status:
            order_id = res['data']['meta']['order_id']
            try:
                # get order object
                order = Order.objects.get(id=order_id)
                order.status = 3
                order.save()

                # get payment object and update its attributes
                payment = order.payment
                payment.payed_at = datetime.now()
                payment.status = 2
                payment.payment_referance_number = tx_ref
                payment.save()

                # update product
                product = order.product
                product.available_quantity -= order.quantity
                product.save()

            except Order.DoesNotExist:
                raise Http404
            redirect_url = reverse('track_order', args=[order_id])
            return redirect(redirect_url)

    order = Order.objects.get(id=order_id)
    messages.add_message(request, messages.ERROR, "Transaction Failed")
    return render(request, template_name='checkout/checkout.html', context={"order": order})
