from django.db import models
from accounts.models import User

# Create your models here.
class Amapoints(models.Model):
    user            = models.ForeignKey(User, on_delete=models.CASCADE,
                                        verbose_name='User')
    points          = models.IntegerField()

    def __str__(self):
        return str(self.user)
