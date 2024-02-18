from django.contrib import admin
from django.http import HttpRequest

from store.models import Payout, Store, Plan, Subscription, SubscriptionPayment


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "code",
        "created_at",
        "price",
    ]

    def has_view_permission(self, request: HttpRequest, obj=None) -> bool:
        return request.user.is_authenticated and request.user.is_admin

    def has_add_permission(self, request: HttpRequest, obj=None) -> bool:
        return request.user.is_authenticated and request.user.is_admin

    def has_delete_permission(self, request: HttpRequest, obj=None) -> bool:
        return request.user.is_authenticated and request.user.is_admin

    def has_change_permission(self, request: HttpRequest, obj=None) -> bool:
        return request.user.is_authenticated and request.user.is_admin

    def has_module_permission(self, request: HttpRequest, obj=None) -> bool:
        return request.user.is_authenticated and request.user.is_admin


@admin.register(SubscriptionPayment)
class SubscriptionPaymentAdmin(admin.ModelAdmin):
    list_display = [
        "subscription",
        "amount",
        "store",
        "added_at",
        "status",
    ]

    def has_view_permission(self, request: HttpRequest, obj=None) -> bool:
        return request.user.is_authenticated and request.user.is_admin

    def has_add_permission(self, request: HttpRequest, obj=None) -> bool:
        return request.user.is_authenticated and request.user.is_admin

    def has_delete_permission(self, request: HttpRequest, obj=None) -> bool:
        return request.user.is_authenticated and request.user.is_admin

    def has_change_permission(self, request: HttpRequest, obj=None) -> bool:
        return request.user.is_authenticated and request.user.is_admin

    def has_module_permission(self, request: HttpRequest, obj=None) -> bool:
        return request.user.is_authenticated and request.user.is_admin


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = [
        "plan",
        "created_at",
        "store",
        "subscription_code",
        "status",
        "canceled_at",
    ]

    def has_view_permission(self, request: HttpRequest, obj=None) -> bool:
        return request.user.is_authenticated and request.user.is_admin

    def has_add_permission(self, request: HttpRequest, obj=None) -> bool:
        return request.user.is_authenticated and request.user.is_admin

    def has_delete_permission(self, request: HttpRequest, obj=None) -> bool:
        return request.user.is_authenticated and request.user.is_admin

    def has_change_permission(self, request: HttpRequest, obj=None) -> bool:
        return request.user.is_authenticated and request.user.is_admin

    def has_module_permission(self, request: HttpRequest, obj=None) -> bool:
        return request.user.is_authenticated and request.user.is_admin


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):

    def approve_selected_stores(self, request, queryset):
        for store in queryset:
            u = store.owner
            u.is_seller = True
            u.staff = True
            u.save()

            store.is_approved = True
            store.save()

    actions = [
        "approve_selected_stores",
    ]

    list_filter = [
        "is_approved",
        "is_registered",
    ]

    list_display = [
        "business_name",
        "business_address",
        "owner",
        "email",
        "alternate_email",
        "phone_number",
        "alternate_phone_number",
        "about",
        "is_registered",
        "created_at",
        "is_approved",
        "is_verified",
        "is_open",
        "last_viewed",
    ]

    def has_module_permission(self, request: HttpRequest, obj=None) -> bool:
        return request.user.is_authenticated and request.user.is_admin

    def has_view_permission(self, request: HttpRequest, obj=None) -> bool:
        return request.user.is_authenticated and request.user.is_admin

    def has_add_permission(self, request, obj=None):
        return request.user.is_authenticated and request.user.is_admin

    def has_delete_permission(self, request, obj=None):
        return request.user.is_authenticated and request.user.is_admin

    def has_change_permission(self, request, obj=None):
        return request.user.is_authenticated and request.user.is_admin


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
        return request.user.is_authenticated and (
            request.user.is_admin or request.user.is_seller
        )

    def has_view_permission(self, request: HttpRequest, obj=None) -> bool:
        return request.user.is_authenticated and (
            request.user.is_admin
            or ((obj and obj.store == request.user.store) or obj is None)
        )

    def has_add_permission(self, request, obj=None):
        return request.user.is_authenticated and request.user.is_admin

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
