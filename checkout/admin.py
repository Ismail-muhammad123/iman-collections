import imp
from django.contrib import admin
from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    def order_id(self, obj):
        return obj.order.id

    list_display = [
        "amount",
        "payment_referance_number",
        "transaction_ref",
        "created_at",
        "payed_at",
        "status",
    ]

    search_fields = [
        "order__id",
    ]

    def has_add_permission(self, request, obj=None):
        return request.user.is_admin

    def has_delete_permission(self, request, obj=None):
        return request.user.is_admin

    def has_change_permission(self, request, obj=None):
        return request.user.is_admin
