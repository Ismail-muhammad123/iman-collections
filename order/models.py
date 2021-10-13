from django.db import models

from products.models import Supplier

# Create your models here.


class Order(models.Model):
    # TODO set the order relation to the cumstomer account
    
    date_added = models.DateTimeField(auto_now_add=True)
    quentity = models.IntegerField()
    total_amount = models.FloatField()
    product = models.ForeignKey("products.Product", on_delete=models.DO_NOTHING)
    delivery_date = models.DateField()
    supplier = models.ForeignKey("products.Suplier", on_delete=models.DO_NOTHING)
    tailor_reciever = models.ForeignKey("products.Suplier", null=True, on_delete=models.DO_NOTHING)