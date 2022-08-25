from django.db import models
from order.models import Order


class Payment(models.Model):

    STATUS_CHOICES = [
        (0, "failed"),
        (1, "Pending"),
        (2, "Success"),
    ]

    order = models.OneToOneField(
        Order, on_delete=models.CASCADE, related_name='payment')
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    delivery_address = models.TextField()
    email = models.EmailField(null=True)
    payment_referance_number = models.CharField(max_length=200)
    amount = models.FloatField()
    country = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=10)
    state = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)
    payed_at = models.DateTimeField(null=True)
    status = models.PositiveIntegerField(choices=STATUS_CHOICES, default=1)
