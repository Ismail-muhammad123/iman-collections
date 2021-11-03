from django.contrib import admin
from .models import Order, OrderProduct
from django.urls import reverse


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "email",
        "address",
        "mobile_number",
        "amount",
        "payment",
        "quantity",
        "discount",
        "delivery_date",
        "status",
        "customer",
        "date_added",
    ]


@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = [
        "item",
        "quantity",
        "size",
        "order",
        "user",
        "date_added"
    ]
