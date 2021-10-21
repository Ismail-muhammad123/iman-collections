from django.db import models
from django.conf import settings

# Create your models here.


class Payment(models.Model):
    STATUS_CHOICES = [
        (1, "SUCCESS"),
        (0, "FAILED")
    ]
    refrence_code = models.CharField(max_length=200)
    status = models.IntegerField(choices=STATUS_CHOICES, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)

