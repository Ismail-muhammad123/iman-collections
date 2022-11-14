from datetime import datetime
from django.conf import settings
from django.utils.timezone import make_aware
from json import JSONDecoder
from pprint import pprint
from django.shortcuts import render, redirect
from django.conf import settings
import uuid
from django.shortcuts import get_object_or_404

from products.models import Cart
from .models import Payment
from order.models import Order
import requests
from django.contrib import messages
from django.urls import reverse
from django.http import Http404, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required


def checkout(request, order_id):

    unique_id = str(uuid.uuid4())

    verification_url = settings.REDIRECT_URL

    device = request.COOKIES['device']

    order = get_object_or_404(Order, id=order_id)

    if order.user == request.user or order.device == device:

        if request.user.is_authenticated:
            email = request.user.email
            full_name = request.user.get_full_name()
            phone_number = request.user.mobile_number
        else:
            email = order.email
            full_name = order.full_name
            phone_number = order.phone_number

        payment, created = Payment.objects.get_or_create(
            order=order,
            defaults={
                "payment_referance_number": unique_id,
                "amount": order.total_amount
            }
        )

        if not created:
            if payment.status == 2:
                messages.add_message(
                    request, messages.INFO, "The payment for this order has already been completed.")
                return render(request, "order/new_order.html")

        if request.user.is_authenticated:
            payment.user = request.user
        else:
            payment.device = device

        payment.save()

        url = settings.PAYMENT_GATEAWAY_URL
        secret_key = settings.PAYMENT_GATEAWAY_SECRET_KEY

        headers = {"Authorization": f"Bearer {secret_key}"}

        data = {
            "reference": unique_id,
            'email': email,
            "amount": order.total_amount * 100,
            "currency": "NGN",
            "callback_url": verification_url,
            "metadata": {
                "order_id": order.id,
                "customer": {
                    "email": email,
                    "phone_number": phone_number,
                    "name": full_name
                },
            },
        }
        res = requests.post(url, headers=headers, json=data)
        response = res.json()
        print(response['status'])
        print(response)
        if response['status'] == True:
            return redirect(response['data']['authorization_url'])
        else:
            # pprint(response)
            return redirect(reverse("new_order"))
    else:
        raise Http404()


def verify_payment(request):
    headers = {"Authorization": f"Bearer {settings.PAYMENT_GATEAWAY_SECRET_KEY}"}
    data = request.GET

    tx_ref = data['trxref']
    response = requests.get(
        settings.PAYMENT_VERIFICATION_URL + tx_ref, headers=headers)
    # print(response.status_code)
    if response.status_code == 200:
        res = response.json()
        status = res['data']['log']['success']
        # print(status)
        if status:
            order_id = res['data']['metadata']['order_id']
            # get order object
            order = get_object_or_404(Order, id=order_id)
            order.status = 3
            order.save()

            # get payment object and update its attributes
            payment = order.payment
            payed_at = datetime.now()
            aware_datetime = make_aware(payed_at)
            payment.payed_at = aware_datetime
            payment.status = 2
            payment.transaction_ref = tx_ref
            payment.save()

            # update product
            sold_products = order.order_items.all()
            for item in sold_products:
                p = item.product
                try:
                    p.available_quantity -= item.quantity
                except:
                    p.available_quantity = 0

                p.save()

            # except Order.DoesNotExist:
            #     raise Http404
            # empty the cart

            cart = request.user.cart if request.user.is_authenticated else Cart.objects.filter(
                device=request.COOKIES['device'])

            [item.delete() for item in cart]

            # redirect to order-tracking page
            return redirect(reverse('track_order'))
        else:
            print(res['data']['metadata'])
            order = Order.objects.get(id=order_id)
            order.delete()
            return render(request, "checkout/payment_failed.html")

    else:
        return render(request, "checkout/payment_failed.html")

    # messages.add_message(request, messages.ERROR, "Traonsaction has Failed")
    # return render(request, template_name='base/index.html')
