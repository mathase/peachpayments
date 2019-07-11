from django.conf.urls import url, include

from accounts import views

app_name = 'accounts'
urlpatterns = [
    url(r'^api/',views.UserListView.as_view()),
    url(r'^api2/',include('django.contrib.auth.urls')),
    url(r'^register',views.register, name='register'),
    
]