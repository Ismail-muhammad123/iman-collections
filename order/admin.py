from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    def name(self, obj):
        return obj.product.name

    def price(self, obj):
        return obj.product.price

    list_display = [
        "name",
        "price",
        "quantity",
        "date_added",
        "total_amount",
        "delivery_date",
        "status",
    ]
