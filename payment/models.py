from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Payment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="payments")
    amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    payed_at = models.DateTimeField(auto_now_add=True)
    payment_referance_number = models.CharField(max_length=200)
    status = models.PositiveIntegerField()

    delivery_address = models.TextField(blank=True, default="")
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(blank=True, default="")
    state = models.CharField(max_length=20)
