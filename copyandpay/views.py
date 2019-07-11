# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.conf import settings

from django.shortcuts import redirect
from .models import Transaction, Product, Customer
from .helpers import prepare_checkout_data, handle_transaction_result, post_to_slack, get_receipt_context
from .appointmentguru import AppointmentGuru
from orders.models import Order

import requests, json

def index(request):
    '''
    Purchase a product
    '''
    products = Product.objects.all()
    context = {
        "page_title": "Choose a product",
        "products": products
    }
    return render(request, 'copyandpay/products.html', context=context)

#, product_id
def prep(request):
    data = ''
    total = 0
    # if record exists remove memebrship section
    # remove_membership_sign_up = 'True'
    data = Order.objects.filter(user = request.user)
    count = Order.objects.filter(user = request.user).count()
    
   
    total = 0
    for info in data:
        total = total + float(info.price)
     
    from copyandpay.models import Product

    if(Product.objects.filter(user = request.user.email).exists() == True):
        pro  = Product.objects.get(user = request.user.email)
        pro.delete()

        product = Product()
        product.currency = 'ZAR'
        product.title = request.user.email
        product.user = request.user.email
        product.price = total
        product.is_recurring = True
        product.save()
    else:
        product = Product()
        product.currency = 'ZAR'
        product.title = request.user.email
        product.user = request.user.email
        product.price = total
        product.is_recurring = True
        product.save()

    

    pay = Product.objects.get(user=request.user.email)
    product_id = pay.id
    payment_page(request, product_id)

    return redirect('/pay/'+str(product_id))

def payment_page(request, product_id):
    
    data = ''
    total = 0
    # if record exists remove memebrship section
    # remove_membership_sign_up = 'True'
    dataC = Order.objects.filter(user = request.user)
    count = Order.objects.filter(user = request.user).count()
    
   
    total = 0
    for info in dataC:
        total = total + float(info.price)

    '''
    Once off payment

    curl https://oppwa.com/v1/checkouts \
    -d "authentication.userId=8acda4ca6b26d8dc016b6ad811564e38" \
    -d "authentication.password=d6sqWACDTR" \
    -d "authentication.entityId=8acda4c86b26d8dd016b6ad89c8d45aa" \
    -d "amount=92.00" \
    -d "currency=ZAR" \
    -d "paymentType=DB"
    '''

    token = request.GET.get('t', None)
    user_data = None
    if token is not None:
        guru = AppointmentGuru(token)
        me = guru.me()
        user_data = me.json().get('results')[0]

    product = Product.objects.get(id=product_id)
    data = prepare_checkout_data(request, user_data, product)

    url = 'https://oppwa.com/v1/checkouts'

    print(url)
    print(data)
    response = requests.post(url, data)
    checkout_id = response.json().get('id')
    context = {
        'peach_base_url': 'https://oppwa.com/',
        'result_url': 'http://localhost:8000/result/',
        'checkout_id': checkout_id,
        'me': user_data,
        'product': product,
        'dataC':dataC, 'count':count, 'total':total
    }
    return render(request, 'dashboard/pages/cart.html', context=context)

def result_page(request):

    base = 'https://oppwa.com/'
    path = request.GET.get('resourcePath')
    url = '{}{}'.format(base, path)
    payment_result = requests.get(url)
    payment_data = payment_result.json()
    # try:
    post_to_slack(payment_data)
    # except Exception:
    #     pass

    if payment_data.get('id', None) is not None:
        result_data = payment_result.json()
        transaction = Transaction.from_peach_response(result_data)
        handle_transaction_result(transaction, send_to_slack=False)
    else:
        # error
        pass

    context = {
        'company': 'AppointmentGuru',
        'result': payment_data
    }
    return render(request, 'copyandpay/result.html', context=context)

def transaction_receipt(request, id):
    transaction_id = request.GET.get('key', None)
    transaction = get_object_or_404(
        Transaction,
        pk=id,
        transaction_id=transaction_id)
    context = get_receipt_context(transaction)
    return render(request, 'copyandpay/receipt.html', context=context)
