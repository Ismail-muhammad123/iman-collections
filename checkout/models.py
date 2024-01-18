from django.db import models
from order.models import Order
from django.contrib.auth import get_user_model


User = get_user_model()


class Payment(models.Model):
    STATUS_CHOICES = [
        (0, "failed"),
        (1, "Pending"),
        (2, "Success"),
    ]

    order = models.OneToOneField(
        Order,
        on_delete=models.CASCADE,
        related_name="payment",
        null=True,
    )
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="payments"
    )
    device = models.CharField(max_length=100, null=True, blank=True, default="")
    payment_referance_number = models.CharField(max_length=200)
    amount = models.FloatField()
    transaction_ref = models.CharField(max_length=250, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    payed_at = models.DateTimeField(null=True)
    status = models.PositiveIntegerField(choices=STATUS_CHOICES, default=1)

    def __str__(self) -> str:
        return self.order
