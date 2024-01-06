from email.policy import default
from django.db import models
from django.contrib.auth import get_user_model

from products.models import Product, ProductVariant
from store.models import Store


# from products.models import Suplier

User = get_user_model()


class Order(models.Model):
    STATUS_CHOICES = [
        (1, "Canceled"),
        (2, "Recieved"),
        (3, "Processing"),
        (4, "Pending"),
    ]

    DELIVERY_STATUS_CHOICES = [
        (1, "Unfulfiled"),
        (2, "Fulfiled"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        default="",
        null=True,
        related_name="orders",
    )

    seller = models.ForeignKey(
        Store, on_delete=models.SET_NULL, null=True, related_name="orders"
    )

    country = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=10, null=True)
    delivery_address = models.TextField()

    full_name = models.CharField(max_length=200, blank=True, default="", null=True)
    email = models.EmailField(blank=True, default="", null=True)
    phone_number = models.CharField(max_length=20, blank=True, default="", null=True)

    device = models.CharField(max_length=100, default="", blank=True, null=True)
    tracking_id = models.CharField(max_length=10, null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    delivery_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.PositiveIntegerField(choices=STATUS_CHOICES, default=4)
    delivery_status = models.PositiveIntegerField(
        choices=DELIVERY_STATUS_CHOICES, default=1
    )
    delivery_date = models.DateField(null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def items(self):
        return self.order_items.all()

    def __str__(self) -> str:
        return f"Order {self.id}"


class OrderItem(models.Model):
    product = models.ForeignKey(
        ProductVariant, on_delete=models.DO_NOTHING, related_name="orders"
    )
    quantity = models.PositiveBigIntegerField()
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="order_items"
    )

    def __str__(self) -> str:
        return self.product.name
