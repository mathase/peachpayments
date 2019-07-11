from django.db import models
from django.contrib.auth.models import AbstractUser
#from reps.models import Rep

#from reps.models import Rep

class User(AbstractUser):
    first_name  = models.CharField(blank=True, max_length=255)
    last_name   = models.CharField(blank=True, max_length=255)
    rep         = models.CharField(blank=True, max_length=255)
    email       = models.EmailField()
    phone       = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.email
