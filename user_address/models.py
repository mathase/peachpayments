from django.db import models
from accounts.models import User
from orders.models import Order

# Create your models here.
class User_Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                                        verbose_name='User')
    #user_address_id = models.CharField(max_length=100, unique=True)
    address_number = models.CharField (max_length=100)
    address_street_name = models.CharField (max_length=100)
    address_suburb = models.CharField (max_length=200)
    city = models.CharField (max_length=100)
    province = models.CharField (max_length=100)
    country = models.CharField (max_length=100)
    postal_code = models.CharField(max_length=100)
    #order_id = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Order')

    def __str__(self):
        return str(self.user)