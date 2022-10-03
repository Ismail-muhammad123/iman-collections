from email.policy import default
from django.db import models
from django.contrib.auth import get_user_model

from products.models import Product


# from products.models import Suplier

User = get_user_model()


class Order(models.Model):

    STATUS_CHOICES = [
        (1, "Canceled"),
        (2, "Recieved"),
        (3, "Processing"),
        (4, "Pending"),
    ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="orders")
    country = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=10, blank=True, default="")
    delivery_address = models.TextField()

    tracking_id = models.CharField(max_length=10, null=True)
    total_amount = models.FloatField()
    status = models.PositiveIntegerField(choices=STATUS_CHOICES, default=4)
    delivery_date = models.DateField(null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def items(self):
        return self.order_items.all()


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.DO_NOTHING, related_name="orders")
    quantity = models.PositiveBigIntegerField()
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="order_items")
