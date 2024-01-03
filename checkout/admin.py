from typing import Any
from django.contrib import admin
from django.http.request import HttpRequest
from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    def order_id(self, obj):
        return obj.order.id

    list_display = [
        "id",
        "amount",
        "transaction_ref",
        "created_at",
        "payed_at",
        "status",
    ]

    search_fields = ["id", "order__id", "transaction_ref"]

    list_filter = [
        "created_at",
        "payed_at",
        "status",
    ]

    def has_view_permission(self, request, obj=None) -> bool:
        return request.user.is_admin

    def has_add_permission(self, request, obj=None):
        return request.user.is_admin

    def has_delete_permission(self, request, obj=None):
        return request.user.is_admin

    def has_change_permission(self, request, obj=None):
        return request.user.is_admin
