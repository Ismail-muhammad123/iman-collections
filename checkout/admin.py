import imp
from django.contrib import admin
from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    def order_id(self, obj):
        return obj.order.id

    list_display = [
        "order_id",
        "amount",
        "payment_referance_number",
        "created_at",
        "payed_at",
        "status",
    ]
