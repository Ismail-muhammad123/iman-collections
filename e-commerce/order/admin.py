from typing import Any
from django.contrib import admin
from django.http.request import HttpRequest
from django.urls import reverse
from .models import Order, OrderItem
from django.utils.safestring import mark_safe
from checkout.models import Payment
from products.models import Product, ProductVariant


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    def name(self, obj):
        if obj.user:
            return f"{obj.user.first_name} {obj.user.last_name}"
        else:
            return obj.full_name

    def payment_status(self, obj):
        if obj.payment:
            display_text = "<a href={}>{}</a>".format(
                reverse(
                    "admin:{}_{}_changelist".format(
                        Payment._meta.app_label, Payment._meta.model_name
                    ),
                )
                + f"?q={obj.pk}",
                obj.payment.get_status_display(),
            )
        else:
            display_text = "-"

        if display_text:
            return mark_safe(display_text)
        return "-"

    def items(self, obj):
        display_text = "<a href={}>{}</a>".format(
            reverse(
                "admin:{}_{}_changelist".format(
                    OrderItem._meta.app_label, OrderItem._meta.model_name
                ),
            )
            + f"?q={obj.pk}",
            f"View Items",
        )

        if display_text:
            return mark_safe(display_text)
        return "-"

    list_display = [
        "id",
        "name",
        "status",
        "items",
        "payment_status",
        "country",
        "state",
        "zip_code",
        "delivery_address",
        "by",
    ]

    list_filter = [
        "date_added",
    ]

    # actions = [

    # ]

    def payment_status(self, obj):
        if obj.payment:
            display_text = "<a href={}>{}</a>".format(
                reverse(
                    "admin:{}_{}_changelist".format(
                        Payment._meta.app_label, Payment._meta.model_name
                    ),
                )
                + f"?q={obj.pk}",
                obj.payment.get_status_display(),
            )
        else:
            display_text = "-"

        if display_text:
            return mark_safe(display_text)
        return "-"

    def by(self, obj):
        return obj.user if obj.user else "Guest"

    def has_view_permission(self, request: HttpRequest, obj=None) -> bool:
        return (
            request.user.is_authenticated
            and request.user.is_admin
            or (obj and obj.seller == request.user.store)
        )

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    def buyer(self, obj):
        if obj.order.user:
            return f"{obj.order.user.first_name} {obj.order.user.last_name}"
        else:
            return obj.order.full_name

    def date(self, obj):
        return obj.order.date_added

    def price(self, obj):
        return obj.product.price

    def brand(self, obj):
        return obj.product.product.brand_name

    def size(self, obj):
        return obj.product.size

    def color(self, obj):
        return obj.product.color

    def product_image(self, obj):
        display_text = "<a href={}>{}</a>".format(
            reverse(
                "admin:{}_{}_changelist".format(
                    ProductVariant._meta.app_label, ProductVariant._meta.model_name
                ),
            )
            + f"?q={obj.product.pk}",
            f"<img src={obj.product.image.url} width='100px' height='100px'/>",
        )

        if display_text:
            return mark_safe(display_text)
        return "-"

    def order_delivery_status(self, obj):
        style = (
            "background-color: orange;"
            if obj.delivery_status == 1
            else "background-color: green;"
        )

        display_text = (
            f"<div style='{style}'>{obj.get_delivery_status_display()} </div>"
        )

        if display_text:
            return mark_safe(display_text)
        return "-"

    def has_view_permission(self, request, obj=None) -> bool:
        return (
            request.user.is_authenticated
            and request.user.is_admin
            or (obj and obj.product.store == request.user.store)
        )

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return request.user.is_authenticated and request.user.is_admin

    def mark_as_fullfiled(self, request, queryset):
        for obj in queryset:
            obj.delivery_status = 2
            obj.save()

    def mark_as_unfullfiled(self, request, queryset):
        for obj in queryset:
            obj.delivery_status = 1
            obj.save()

    actions = [
        "mark_as_fullfiled",
        "mark_as_unfullfiled",
    ]

    list_display = [
        "product",
        "size",
        "color",
        "buyer",
        "price",
        "tax",
        "delivery_fee",
        "tracking_id",
        "order_delivery_status",
        "delivery_date",
        "quantity",
        "date",
        "product_image",
    ]

    list_display_links = []

    list_filter = [
        "delivery_status",
    ]

    search_fields = [
        "order__id",
    ]
