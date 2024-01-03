from django.contrib import admin
from django.http import HttpRequest

from store.models import Payout, Store

# Register your models here.


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "business_name",
        "address",
        "owner",
        "email",
        "alternate_email",
        "phone_number",
        "alternate_phone_number",
        "bio",
        "about",
        "is_registered",
        "created_at",
        "rc_number",
        "registration_certificate",
        "is_verified",
        "is_open",
        "last_viewed",
    ]

    def has_module_permission(self, request: HttpRequest, obj=None) -> bool:
        return request.user.is_admin or request.user.is_seller

    def has_view_permission(self, request: HttpRequest, obj=None) -> bool:
        return request.user.is_admin or obj == request.user.store

    def has_add_permission(self, request, obj=None):
        return request.user.is_admin or obj == request.user.store

    def has_delete_permission(self, request, obj=None):
        return request.user.is_admin or obj == request.user.store

    def has_change_permission(self, request, obj=None):
        return request.user.is_admin or obj == request.user.store


@admin.register(Payout)
class PayoutAdmin(admin.ModelAdmin):
    list_display = [
        "currency",
        "amount",
        "store",
        "bank_name",
        "account_name",
        "account_number",
        "time",
        "added_by",
    ]

    def has_module_permission(self, request: HttpRequest, obj=None) -> bool:
        return request.user.is_admin or request.user.is_seller

    def has_view_permission(self, request: HttpRequest, obj=None) -> bool:
        return request.user.is_admin or obj.store == request.user.store

    def has_add_permission(self, request, obj=None):
        return request.user.is_admin or obj.store == request.user.store

    def has_delete_permission(self, request, obj=None):
        return request.user.is_admin or obj.store == request.user.store

    def has_change_permission(self, request, obj=None):
        return request.user.is_admin or obj.store == request.user.store
