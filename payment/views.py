from django.contrib.auth import login
from django.shortcuts import redirect, render
from cart.models import Cart
from django.contrib.auth.decorators import login_required
import requests
import json
from django.conf import settings
from payment.models import Payment


# Create your views here.Content-Type

@login_required
def checkout(request):
    cart_items = Cart.objects.all().filter(user=request.user)
    total_quantity = 0.0
    total_price = 0.0
    total_amount = 0.0
    user_email = request.user.email

    items = []

    for i in cart_items:
        items.append([
            i.item.name,
            i.quantity,
            i.item.price,
            i.item.price * i.quantity,
        ])

        total_price =+ i.item.price
        total_quantity += i.quantity
        total_amount += i.item.price * i.quantity

    context = {
        'cart_items' : items,
        'total_quantity' : total_quantity,
        'total_price' : total_price,
        'total_amount' : total_amount,
        'user_email' : user_email,

    }


    return render(request, template_name='payment/checkout.html', context=context)

@login_required
def success(request):
    data = request.GET.dict()

    print(dict(data))

    ref = data['reference']

    trxref = data['trxref']

    req = requests.get('https://api.paystack.co/transaction/verify/'+ref, headers={
        "Authorization": "Bearer " + settings.PAYSTACK_SECRET_KEY
    })

    print('response status: ', req.status_code)
    print('data: ', req.text)
    if req.status_code == 200:
        result = json.loads(req.text)
        print(result)
        if result['data']['status']:
            print("payment successfull")
            return render(request, 'payment/success.html')
        else:
            return render(request, 'payment/canceled.html')

    else:
        return render(request, 'payment/canceled.html')

@login_required
def canceled(request):
    return render(request, 'payment/canceled.html')

@login_required
def initialize(request):
    req = requests.post(url='https://api.paystack.co/transaction/initialize', data=json.dumps({
        "email": "ismaeelmuhammad123@gmail.com", "amount": "1000"
    }), headers={
        "Authorization": "Bearer "+settings.PAYSTACK_SECRET_KEY,
        "Content-Type": "application/json"
    })


    print(req.text)
    if req.status_code != 200:
        return canceled(request)

    result = json.loads(req.text)

    print(result)

    if result['status'] == True:
        p = Payment.objects.create(
            user=request.user,
            refrence_code = result['data']['reference']
        )
        p.save()
        return redirect(result['data']['authorization_url'])