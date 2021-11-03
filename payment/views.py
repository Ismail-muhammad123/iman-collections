from django.contrib import messages
from django.shortcuts import redirect, render
from cart.models import Cart
from django.contrib.auth.decorators import login_required
from django.conf import settings
from payment.models import Payment
from order.models import Order, OrderProduct

import datetime
import requests
import json


# Create your views here.Content-Type

@login_required
def checkout(request):
    cart_items = Cart.objects.all().filter(user=request.user)
    total_quantity = 0.0
    total_price = 0.0
    total_amount = 0.0

    items = []

    for i in cart_items:
        items.append([
            i.item.name,
            i.quantity,
            i.item.price,
            i.item.price * i.quantity,
        ])

        total_price = + i.item.price
        total_quantity += i.quantity
        total_amount += i.item.price * i.quantity

    context = {
        'cart_items': items,
        'total_quantity': total_quantity,
        'total_price': total_price,
        'total_amount': total_amount,
        'user': request.user,

    }
    return render(request, template_name='payment/checkout.html', context=context)


@login_required
def success(request):

    # get the response params
    data = request.GET.dict()

    ref = data['reference']
    trxref = data['trxref']

    # verify transaction on paystack api with the params recieved
    req = requests.get('https://api.paystack.co/transaction/verify/'+ref, headers={
        "Authorization": "Bearer " + settings.PAYSTACK_SECRET_KEY
    })

    # if request succreeded
    if req.status_code == 200:
        result = json.loads(req.text)
        # print(result)

        payment = Payment.objects.get(
            refrence_code=result['data']['reference'])
        order = Order.objects.get(payment=payment)

        # if verified
        if result['data']['status']:
            # print("payment successfull")

            res = result['data']
            # set current transaction payment object fields
            # with data from the verify-transaction response
            # and then save it
            payment.status = 1
            payment.currency = res['currency']
            payment.channel = res['channel']
            payment.card_type = res['authorization']['card_type']
            payment.bank = res['authorization']['bank']
            payment.card_last_four = res['authorization']['last4']
            payment.country_code = res['authorization']['country_code']
            payment.account_name = res['authorization']['account_name']
            payment.save()

            # set order status to processing
            # and save it
            order.status = 'PRC'
            order.save()

            # clear user's cart
            cart = Cart.objects.all().filter(user=request.user)
            for c in cart:
                i = c.item
                i.available_quantity = i.available_quantity - c.quantity
                i.quantity_sold = i.quantity_sold + c.quantity
                i.save()
                c.delete()

            messages.success(request, "Your purchase was successful")

            return redirect('/order')

        else:
            # set payment status to failed
            payment.status = 0
            return redirect('/canceled.html')

    else:
        messages.error(request, 'Your Payment was canceled')
        return redirect('/payment')


@login_required
def canceled(request):
    return render(request, 'payment/canceled.html')


@login_required
def initialize(request):

    # extraxt the data sent from the form in the webpage
    data = request.POST.dict()
    email = data['email']
    phone_number = data['phone_number']
    delivery_address = data['delivery_address']
    full_name = data['full_name']
    amount = data['total_amount']
    quantity = float(data['total_quantity'])

    # get the items currently in the cart of user
    cart_items = Cart.objects.filter(user=request.user)
    print(cart_items)

    # create a new Order object and add the order information
    new_order = Order.objects.create(email=email,
                                     name=full_name,
                                     address=delivery_address,
                                     mobile_number=phone_number,
                                     customer=request.user,
                                     quantity=quantity,
                                     amount=float(amount)
                                     )
    new_order.amount = float(amount)
    print('cart_items:')

    # send a transaction initialization request to paystack with the current email and amount
    # and get transaction reference
    req = requests.post(url='https://api.paystack.co/transaction/initialize', data=json.dumps({
        "email": email, "amount": amount
    }), headers={
        "Authorization": "Bearer "+settings.PAYSTACK_SECRET_KEY,
        "Content-Type": "application/json"
    })

    # print(req.text)

    # if request is not successfull, cancel transaction
    if req.status_code != 200:
        return canceled(request)

    result = json.loads(req.text)

    # if transaction initiated successfully
    if result['status'] == True:
        # create a new payment object with the reference from the response
        p = Payment.objects.create(
            user=request.user,
            refrence_code=result['data']['reference'],
            amount=float(amount)
        )
        p.save()

        # set the created transaction object as payment field of the created order object
        new_order.payment = p
        delivery_days = [d.item.delivery_in for d in cart_items]
        days = max(delivery_days)
        new_order.delivery_date = datetime.datetime.today() + datetime.timedelta(days=days)
        new_order.save()

        for c in cart_items:
            item = OrderProduct.objects.create(
                item=c.item,
                quantity=c.quantity,
                size=c.size,
                user=request.user,
                order=new_order
            )
            item.save()

        # reirect to the paystack payment page
        return redirect(result['data']['authorization_url'])
