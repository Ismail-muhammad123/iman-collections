from django.db import models
from django.contrib.auth import get_user_model


# from products.models import Suplier

User = get_user_model()


class Order(models.Model):

    STATUS_CHOICES = [
        (1, "Canceled"),
        (2, "Recieved"),
        (3, "Pending"),
    ]

    # user = models.ForeignKey(
    #     User, on_delete=models.CASCADE, related_name="orders")

    product = models.ForeignKey(
        "products.Product", on_delete=models.CASCADE, related_name="orders")
    quantity = models.PositiveIntegerField()
    total_amount = models.FloatField()
    date_added = models.DateTimeField(auto_now=True)
    status = models.PositiveIntegerField(choices=STATUS_CHOICES, default=3)
    delivery_date = models.DateField(null=True)
