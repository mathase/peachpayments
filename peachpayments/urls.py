from django.conf.urls import url, include
from django.contrib import admin
from copyandpay import views, api
#from django.urls import path, include 

urlpatterns = [
   # url(r'^$', views.index, name='products_page'),
    url(r'^', include('landing.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^dashboard/', include('dashboard.urls')),
    url(r'^api/', include(api.router.urls)),
    url(r'^pay/(?P<product_id>[\w-]+)/$', views.payment_page, name='payment_page'),
    url(r'^transaction/(?P<id>[\w-]+)/$', views.transaction_receipt, name='transaction_receipt'),
    url(r'^result/$', views.result_page, name='result_page'),
    url(r'^admin/', admin.site.urls),

    #
    #url(r'^$', views.landing_page, name='landing_page'),
]
