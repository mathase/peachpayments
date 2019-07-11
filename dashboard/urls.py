from django.conf.urls import url, include
from dashboard import views
from .views import packages, payment, cart, dash, eftPopUp, pay, address, membership, rep
from copyandpay.views import payment_page, prep

app_name = 'dashboard'
urlpatterns = [
    url(r'^packages/', views.packages, name='packages'),
    url(r'^payment/', views.payment, name='payment'),
    url(r'^cart', prep, name='cart'),
    url(r'^dashboard', views.dash, name='dashboard'),
    url(r'^eftPopUp/', views.eftPopUp, name='eftPopUp'),
    url(r'^address/', views.address, name='address'),
    url(r'^pay/$', views.pay, name='pay'),
    url(r'^membership/', views.membership, name='membership'),
    url(r'^rep/', views.rep, name='rep'),
]