from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from accounts.models import User
from django.contrib.auth import authenticate, login
# Create your views here.
def landing_page(request):


    return render(request, 'landing/pages/home.html', {})

def login_in(request):
    if request.method == 'GET':
        context = ''
        return render(request, 'mytest/login.html', {'context': context})

    elif request.method == 'POST':
        username = request.POST.get('email', '')
        password = request.POST.get('password', '')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/dashboard/packages')
            # return HttpResponseRedirect('/')
        else:
            context = {'error': 'Wrong credintials'}  # to display error?
            return render(request, '/registration', {'context': context})

def reg_page(request):

    pass_c = ''
    email_c= ''
    password_validation= 'Confirm Password'
    email_validation  = 'Email'
    if request.POST:
        user_create = User()
        user_create.username = request.POST['email']
        user_create.email = request.POST['email']
        user_create.first_name = request.POST['first_name']
        user_create.last_name = request.POST['last_name']
        user_create.rep = request.POST['rep_id']
        user_create.phone = request.POST['phone']
        user_create.save()
        return redirect('dashboard/packages')
    else:
        pass
    return render(request, 'landing/pages/registration_page.html', {'password_validation':password_validation , 'email_validation':email_validation, 'pass_c':pass_c,'emai_c':email_c})
 

def referral(request):

    
    return render(request, 'landing/pages/referral.html', {})
