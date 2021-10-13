from django.db import models

from products.models import Suppliers

# Create your models here.


class Cart(models.Model):
    #TODO: set the relation of Cart to a customer account
    
    item = models.ForeignKey("products.Product", on_delete=models.DO_NOTHING)
    supplier = models.ForeignKey("products.Suplier")

    quentity = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)


