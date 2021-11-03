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

    # def order_products_list(self, obj):
    #     id = obj.id
    #     change_url = reverse('admin:order_orderProduct_changelist', args=(id,))
    #     return "<a href='{}' target=_blank> Products</a>"


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
