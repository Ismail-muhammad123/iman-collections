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
        "order_products",
        "amount",
        "payment",
        "quantity",
        "discount",
        "delivery_date",
        "status",
        "customer",
        "date_added",
    ]

    def order_products(self, obj):
        return ", ".join([
            f'{child.name}  {child.size}  {child.quantity}  <br/>' for child in obj.order_products.all()
        ])
    order_products.short_description = "Products orderd"


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
