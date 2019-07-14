from django.db import models
from accounts.models import User

# Create your models here.

class Order(models.Model):
    user            = models.ForeignKey(User, on_delete=models.CASCADE,
                                        verbose_name='User')
    #order_id        = models.CharField(max_length=100, unique=True)
    product         = models.CharField (max_length=100)
    order_type      = models.CharField(max_length=100, default="type")
    order_level     = models.CharField(max_length=100, default="none")
    price           = models.CharField(max_length=100)
    isRecurring     = models.BooleanField(default=False)
    isSettled       = models.BooleanField(default=False)
    date_created    = models.DateTimeField(auto_now_add = True)
    image           = models.CharField(max_length=100, default="default.jpg")
    ownBox      = models.ImageField(upload_to='lists', default="none")

    school           = models.CharField(max_length=100, default='none')
    grade           = models.CharField(max_length=100, default='none')

    def __str__(self):
        return str(self.user)
