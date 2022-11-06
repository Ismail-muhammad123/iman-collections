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
        "id",
        "order__id",
        "payment_reference_number",
        "transaction_ref"
    ]

    list_filter = [
        "created_at",
        "payed_at",
        "status",
    ]

    def has_add_permission(self, request, obj=None):
        return request.user.is_admin

    def has_delete_permission(self, request, obj=None):
        return request.user.is_admin

    def has_change_permission(self, request, obj=None):
        return request.user.is_admin
