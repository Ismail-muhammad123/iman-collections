from django.contrib import admin
from .models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    def name(self, obj):
        return obj.user.first_name + " " + obj.user.last_name

    def payment_status(self, obj):
        return obj.payment.get_status_display()

    list_display = [
        "name",
        "country",
        "state",
        "zip_code",
        "delivery_address",
        "tracking_id",
        "total_amount",
        "status",
        "payment_status",
        "delivery_date",
        "date_added",
    ]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    def buyer(self, obj):
        return obj.order.user.first_name + " " + obj.order.user.last_name

    def date(self, obj):
        return obj.order.date_added

    def price(self, obj):
        return obj.product.price

    list_display = [
        "product",
        "buyer",
        "price",
        "quantity",
        "date",
    ]
