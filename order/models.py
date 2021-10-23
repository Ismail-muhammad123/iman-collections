from django.db import models
from django.conf import settings

# Create your models here.


class Order(models.Model):
    # TODO set the order relation to the cumstomer account

    date_added = models.DateTimeField(auto_now_add=True)
    price = models.FloatField()
    discount = models.FloatField()
    quantity = models.IntegerField()
    amount = models.FloatField()
    product = models.ForeignKey(
        "products.Product", on_delete=models.DO_NOTHING)
    delivery_date = models.DateField()
    status = models.CharField(max_length=3)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)