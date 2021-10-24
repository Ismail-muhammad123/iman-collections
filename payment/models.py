from django.db import models
from django.conf import settings

# Create your models here.


class Payment(models.Model):
    STATUS_CHOICES = [
        (1, "SUCCESS"),
        (0, "FAILED")
    ]
    
    amount = models.FloatField()
    currency = models.CharField(max_length=3, null=True,)
    channel = models.CharField(max_length=10, null=True)
    card_type = models.CharField(max_length=10, null=True)
    bank = models.CharField(max_length=30, null=True)
    card_last_four = models.CharField(max_length=4, null=True)
    county_code = models.CharField(max_length=3, null=True)
    account_name = models.CharField(max_length=100, null=True)
    refrence_code = models.CharField(max_length=200)
    status = models.IntegerField(choices=STATUS_CHOICES, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)



