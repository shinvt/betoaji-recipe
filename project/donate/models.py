from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Donation(models.Model):
    donator = models.ForeignKey(User, related_name='donator', on_delete=models.CASCADE)
    donate_amount = models.IntegerField(default=0)
    donate_time = models.DateTimeField(null=True)
