from django.db import models
from django.contrib.auth import get_user_model

# from products.models import Suplier

# Create your models here.

User = get_user_model()


class Cart(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="cart_items")
    item = models.ForeignKey("products.Product", on_delete=models.DO_NOTHING)
    quentity = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
