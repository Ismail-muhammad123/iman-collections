from typing import Sized
from django.db import models

from django.conf import settings

# Create your models here.


class Cart(models.Model):
    item = models.ForeignKey("products.Product", on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    size = models.CharField(max_length=20)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.item.name
