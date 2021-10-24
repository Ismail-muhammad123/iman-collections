from django.db import models
from django.conf import settings
from payment.models import Payment


class OrderProduct(models.Model):
    item = models.ForeignKey("products.Product", on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    size = models.CharField(max_length=20)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.DO_NOTHING)


class Order(models.Model):
    STATUS_CHOICES = [
        ('PND', "Pending"),
        ('PRC', "Processing"),
        ('CMP', "Completed")
    ]

    name = models.CharField(max_length=200)
    email = models.EmailField()
    address = models.TextField()
    mobile_number = models.CharField(max_length=20)

    date_added = models.DateTimeField(auto_now_add=True)
    discount = models.FloatField(default=0.0)
    quantity = models.IntegerField()
    payment = models.OneToOneField(
        Payment, on_delete=models.SET_NULL, null=True, related_name="order_payment")
    amount = models.FloatField()
    products = models.ManyToManyField(
        OrderProduct, related_name="order_products")
    delivery_date = models.DateField(null=True)
    status = models.CharField(max_length=3, default='PND')
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
