from django.shortcuts import render, redirect
from rest_framework import generics

from . import models
from . import serializers
from .models import User
from .forms import CustomUserChangeForm, CustomUserCreationForm

from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from peachpayments.tokens import account_activation_token
from django.core.mail import EmailMessage

from django.contrib.auth import authenticate, login

class UserListView(generics.ListCreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

def register(request):
    form = CustomUserCreationForm
    success_url = '/dashboard/packages'
    template_name = 'landing/pages/registration_page.html'

    username_validation = ''
    email_validation    = ''
    password_validation = ''

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.username = request.POST['email']
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.phone = request.POST['phone']
            user.save()
                
            

            username = request.POST.get('email', '')
            password = request.POST.get('password1', '')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                sendEmail(request)
                return redirect('/dashboard/packages')
            
            


            #return HttpResponse('Please confirm your email address to complete the registration')
            
        else:

            if(User.objects.filter(email = request.POST['email']).exists()):
                email_validation = "email already exists"
                
            if(request.POST['password2'] != request.POST['password1']):
                password_validation = "passwords do not match"

        #return render(request, template_name, 
        #                    {'username_validation':username_validation,
        #                        'email_validation':email_validation,
        #                        'password_validation':password_validation})

        return render
    else:
        #form = SignupForm()
        form_class = CustomUserCreationForm
    return render(request, template_name, {'form': form})
    
def sendEmail(request):
    mail_subject = 'Welcome.'
    message = render_to_string('landing/pages/auth/acc_active_email.html', {})
    to_email = request.user.email
    email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
    email.send()

    


