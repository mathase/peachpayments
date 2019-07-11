from django.conf.urls import url, include
from django.contrib import admin
#from django.urls import path, include 
from django.conf.urls import url, include
from landing import views
from .views import landing_page,login_in,reg_page,referral


app_name = "landing"
urlpatterns = [
    url(r'^$', views.landing_page, name='home'),
    url(r'^log/', views.login_in, name='login'),
    url(r'^registration', views.reg_page, name='registration_page'),
    url(r'^referral', views.referral, name='referral'),
]

