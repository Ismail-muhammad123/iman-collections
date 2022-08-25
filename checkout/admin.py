import imp
from django.contrib import admin
from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    def order_id(self, obj):
        return obj.order.id

    list_display = [
        "first_name",
        "last_name",
        "phone_number",
        "email",
        "order_id",
        "amount",
        "payment_referance_number",
        "delivery_address",
        "country",
        "postal_code",
        "state",
        "created_at",
        "payed_at",
        "status",
    ]
