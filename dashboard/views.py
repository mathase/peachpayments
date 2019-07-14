from django.shortcuts import render, redirect
from django.http import HttpResponse
from amapoints.models import Amapoints
from orders.models import Order
from user_address.models import User_Address
import urllib, json
from flask import Flask
from urllib.request import urlopen, Request
import ssl
import json
from copyandpay.views import payment_page
app = Flask(__name__)

# Create your views here.
def packages(request):
    
    if request.POST:
        order = Order()
        order.user = request.user

    # Foundation ------------------------------------------------------
        # Comprehensive
        if(request.POST['product-name'] == 'comprehensive-foundation'):
            order.image = 'images/foundation.png'
            order.order_level = 'foundation'
            order.order_type = 'stationary'
            order.product = 'Comprehensive(Foundation)'
            if(request.POST['amount-radio'] == 'own-foundation'):
                order.price = request.POST['amount-comprehensive-foundation']
            elif(request.POST['amount-radio'] == 'once-off-foundation'):
                order.price = '1682.52'

        # Essentials
        elif(request.POST['product-name'] == 'essentials-foundation'):
            order.image = 'images/foundation.png'
            order.order_level = 'foundation'
            order.order_type = 'stationary'
            order.product = 'Esentials(Foundation)'
            if(request.POST['amount-radio'] == 'own-essentials'):
                order.price = request.POST['amount-essentials-foundation']
                order.isRecurring = True
            elif(request.POST['amount-radio'] == 'once-off-essentials'):
                order.price = '796.07'

        # MyBox
        elif(request.POST['product-name'] == 'myBox-foundation'):
            order.image = 'images/mybox.png'
            order.order_level = 'foundation'
            order.order_type = 'stationary'
            order.product = 'MyBox(Foundation)'
            order.school = request.POST['school-foundation']
            order.grade = request.POST['grade-foundation']
            order.ownBox = request.FILES['foundation-mybox-list']
            if(request.POST['amount-radio'] == 'own-amount-mybox'):
                order.price = request.POST['amount-mybox-foundation']
                order.isRecurring = True
            elif(request.POST['amount-radio'] == 'once-off-mybox-foundation'):
                order.price = request.POST['av-amount-mybox-foundation']



    # Intermediate ---------------------------------------------------------
        # Comprehensive
        elif(request.POST['product-name'] == 'comprehensive-intermediate'):
            order.image = 'images/intermediate.png'
            order.order_level = 'intermediate'
            order.order_type = 'stationary'
            order.product = 'Comprehensive(Intermediate)'
            if(request.POST['amount-radio'] == 'own-compresenive-intermediate'):
                order.price = request.POST['amount-comprehensive-intermediate']
            elif(request.POST['amount-radio'] == 'once-off-comprehensive-intermediate'):
                order.price = '2402.17'

        # Essentials
        elif(request.POST['product-name'] == 'essentials-intermediate'):
            order.image = 'images/intermediate.png'
            order.order_level = 'intermediate'
            order.order_type = 'stationary'
            order.product = 'Essentials(Intermediate)'
            if(request.POST['amount-radio'] == 'own-essentials-intermediate'):
                order.price = request.POST['amount-essentials-intermediate']
                order.isRecurring = True
            elif(request.POST['amount-radio'] == 'once-off-essentials-intermediate'):
                order.price = '1184.00'
        
        # MyBox
        elif(request.POST['product-name'] == 'mybox-intermediate'):
            order.image = 'images/mybox.png'
            order.order_level = 'intermediate'
            order.order_type = 'stationary'
            order.school = request.POST['school-intermediate']
            order.grade = request.POST['grade-intermediate']
            order.product = 'MyBox(Intermediate)'
            order.ownBox = request.FILES['intermediate-mybox-list']
            if(request.POST['amount-radio'] == 'own-amount-mybox-intermediate'):
                order.price = request.POST['amount-mybox-intermediate']
                order.isRecurring = True
            elif(request.POST['amount-radio'] == 'once-off-mybox-intermediate'):
                order.price = request.POST['av-amount-mybox-intermediate']
        

    # Junior ------------------------------------------------------------------------------
        # Comprehensive
        elif(request.POST['product-name'] == 'comprehensive-junior'):
            order.image = 'images/junorhigh.png'
            order.order_level = 'junior'
            order.order_type = 'stationary'
            order.product = 'Comprehensive(Junior)'
            if(request.POST['amount-radio'] == 'own-comprehensive-junior'):
                order.price = request.POST['amount-comprehensive-junior']
                order.isRecurring = True
            elif(request.POST['amount-radio'] == 'once-off-comprehensive-junior'):
                order.price = '1600.41'
        
        # Essentials
        elif(request.POST['product-name'] == 'essentials-junior'):
            
            order.order_level = 'junior'
            order.order_type = 'stationary'
            order.product = 'Essentials(Junior)'
            if(request.POST['amount-radio'] == 'own-essentials-junior'):
                order.price = request.POST['amount-essentials-junior']
                order.isRecurring = True
            elif(request.POST['amount-radio'] == 'once-off-essentials-junior'):
                order.price = '807.41'

        # MyBox
        elif(request.POST['product-name'] == 'mybox-junior'):
            order.image = 'images/mybox.png'
            order.order_level = 'junior'
            order.order_type = 'stationary'
            order.product = 'MyBox(junior)'
            order.school = request.POST['school-junior']
            order.grade = request.POST['grade-junior']
            order.ownBox = request.FILES['junior-mybox-list']
            if(request.POST['amount-radio'] == 'own-amount-mybox-junior'):
                order.price = request.POST['amount-mybox-junior']
                order.isRecurring = True
            elif(request.POST['amount-radio'] == 'once-mybox-junior'):
                order.price = request.POST['av-amount-mybox-junior']
        
    # Senior ------------------------------------------------------------------------------
        # Comprehensive
        elif(request.POST['product-name'] == 'comprehensive-senior'):
            order.image = 'images/seniorhigh.png'
            order.order_level = 'senior'
            order.order_type = 'stationary'
            order.product = 'Comprehensive(Senior)'
            if(request.POST['amount-radio'] == 'own-comprehensive-senior'):
                order.price = request.POST['amount-comprehensive-senior']
                order.isRecurring = True
            elif(request.POST['amount-radio'] == 'once-off-comprehensive-senior'):
                order.price = '1566.42'
        
        # Essentials
        elif(request.POST['product-name'] == 'essentials-senior'):
            order.image = 'images/seniorhigh.png'
            order.order_level = 'senior'
            order.order_type = 'stationary'
            order.product = 'Essentials(Senior)'
            if(request.POST['amount-radio'] == 'own-essentials-senior'):
                order.price = request.POST['amount-essentials-senior']
                order.isRecurring = True
            elif(request.POST['amount-radio'] == 'once-off-essentials-senior'):
                order.price = '745.14'
        
        # MyBox
        elif(request.POST['product-name'] == 'mybox-senior'):
            order.image = 'images/mybox.png'
            order.order_level = 'mybox-senior'
            order.order_type = 'stationary'
            order.product = 'MyBox(Senior)'
            order.school = request.POST['school-senior']
            order.grade = request.POST['grade-senior']
            order.ownBox = request.FILES['senior-mybox-list']
            if(request.POST['amount-radio'] == 'own-mybox-senior'):
                order.price = request.POST['amount-mybox-senior']
                order.isRecurring = True
            elif(request.POST['amount-radio'] == 'once-off-mybox-senior'):
                order.price = request.POST['av-amount-mybox-average-senior']
                

        
        order.save()
        
        

        return redirect('/dashboard/packages')
    else:
        remove_rep_sign_up = 'False'
        data = ''
        # if record exists remove memebrship section
        if(Order.objects.filter(user = request.user).exists() == True):
            remove_membership_sign_up = 'True'
            data = Order.objects.filter(user = request.user)
            # if rep membership bourg, remove rep dection
            if(Order.objects.filter(user = request.user, order_level='rep').exists() == True):
                remove_rep_sign_up = 'True'
            else:
                remove_rep_sign_up = 'False'

        else:
            remove_membership_sign_up = 'False'
        
        

    args = {'remove_membership_sign_up':remove_membership_sign_up,
            'remove_rep_sign_up':remove_rep_sign_up,
            'data':data}
    return render(request, 'dashboard/pages/packages.html', args)

def membership(request):
    
    order = Order()
    order.image = 'images/logo.jpg'
    order.user = request.user
    order.isRecurring = False
    order.isSettled = False
    order.order_level = 'membership'
    order.price = 99
    order.order_type = 'membership'
    order.product = 'General Membership'
    order.save()

def rep(request):
    order = Order()
    order.image = 'images/representative.png'
    order.user = request.user
    order.isRecurring = False
    order.isSettled = False
    order.order_level = 'rep'
    order.price = 99
    order.product = 'Rep membership'
    order.order_type = 'membership'

    create_rep(request)

    order.save()

def create_rep(request):
    pass
def create_customer(request):
    pass

def payment(request):
    addresses = User_Address.objects.filter(user=request.user)
    order = Order.objects.filter(user = request.user)
    count = Order.objects.filter(user = request.user).count()
    
    total = 0
    for info in order:
        total = total + float(info.price)

        tax = total * 0.15
        allTot = total  + tax

    args ={'addresses':addresses,
            'total':total, 'tax':tax, 'allTot':allTot}
    return render(request, 'dashboard/pages/payment.html', args)

def cart(request):
    
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
        product.currency = 'zar'
        product.title = request.user.email
        product.user = request.user.email
        product.price = total
        product.save()
    else:
        product = Product()
        product.currency = 'zar'
        product.title = request.user.email
        product.user = request.user.email
        product.price = total
        product.save()

    

    pay = Product.objects.get(user=request.user.email)
    product_id = pay.id
    
    payment_page(request, product_id)

    args = {'data':data, 'count':count, 'total':total}
    return render(request, 'dashboard/pages/cart.html', args)

@app.route('/address/')
def address(request):
    if request.POST:
        address = User_Address()
        address.user = request.user

        address.address_number = 'mailing' 
        address.address_street_name = request.POST['address_street_name']
        address.address_suburb = request.POST.get('address_suburb_', False)
        address.city = request.POST['city'] 
        address.province = request.POST['province'] 
        address.country = request.POST['country'] 
        address.postal_code = request.POST['postal_code'] 

        if (request.POST['address_street_name_2'] != ''):
            shipping(request)
        
        address.save()

    return redirect('/dashboard/payment')

def shipping(request):
    address = User_Address()
    address.user = request.user

    address.address_number = 'shipping' 
    address.address_street_name = request.POST['address_street_name_2']
    address.address_suburb = request.POST.get('address_suburb_2', False)
    address.city = request.POST['city_2'] 
    address.province = request.POST['province_2'] 
    address.country = request.POST['country_2'] 
    address.postal_code = request.POST['postal_code_2'] 
    address.save()

def dash(request):

    if (Amapoints.objects.filter(user  = request.user).exists() ==  True ):

        amapoints = Amapoints.objects.get(user  = request.user)

        points = amapoints.points

    else:

        points =  0

        #address = Address.objects.filter(user  = request.user)

        data =  ''
        address =  ''

        total =  0

        # if record exists remove memebrship section

        # remove_membership_sign_up = 'True'

        data = Order.objects.filter(user  = request.user)
        addresses = User_Address.objects.filter(user=request.user)

        args = {'points':points,'data':data,'addresses':addresses}

    return render(request, 'dashboard/pages/dashboard.html', args)



def requestPay():
	url = "https://test.oppwa.com/v1/checkouts"
	data = {
		'entityId' : '8a8294174e735d0c014e78cf26461790',
		'amount' : '92.00',
		'currency' : 'ZAR',
		'paymentType' : 'DB',
        'paymentType' : 'DB',
        'authentication.password' : '8acda4ca6b26d8dc016b6ad811564e38',
        'authentication.entityId' : '0=OGFjZGE0Y2E2YjI2ZDhkYzAxNmI2YWQ4MTE1NjRlMzh8ZDZzcVdBQ0RUUg=='
	}



    #responseData = request();

@app.route('/eftPopUp/')
def eftPopUp(request):
    ssl._create_default_https_context = ssl._create_unverified_context
    url = "https://test.oppwa.com/v1/checkouts"
    data = {
		'entityId' : '8ac7a4c76b691661016b6ae5143a03a4',
		'amount' : '92.00',
		'currency' : 'ZAR',
		'paymentType' : 'DB',
	}
    data_values=urllib.parse.urlencode(data)
    binary_data = data_values.encode(encoding='utf-8')
    try:
        opener = urllib.request.build_opener(urllib.request.HTTPHandler)
        request = urllib.request.Request(url, binary_data)
        request.add_header('Authorization', 'Bearer OGFjN2E0Yzc2YjY5MTY2MTAxNmI2YWU1MGY3ODAzYTJ8M0ZqOHhZbU1RTQ==')
        request.get_method = lambda: 'POST'
        response = opener.open(request)
        
        data = json.loads(response.read().decode('utf-8'))
        return redirect('/dashboard/pay/'+data['id'])
        

    except urllib.request.HTTPError as e:
        return e.code

def pay(request, pay):
    id = pay
    return render(request, 'dashboard/pages/pay.html', {'id':id})
