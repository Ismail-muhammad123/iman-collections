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
        "seller",
        "items",
        "country",
        "state",
        "zip_code",
        "delivery_address",
        "tracking_id",
        "total_amount",
        "status",
        "delivery_status",
        "payment_status",
        "delivery_date",
        "date_added",
        "by",
    ]

    list_filter = [
        "status",
        "delivery_date",
        "date_added",
        "delivery_status",
    ]

    # actions = [

    # ]

    def by(self, obj):
        return obj.user if obj.user else "Guest"

    def has_view_permission(self, request: HttpRequest, obj=None) -> bool:
        return (
            request.user.is_authenticated
            and request.user.is_admin
            or obj.seller == request.user.store
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

    def has_view_permission(self, request, obj=None) -> bool:
        return request.user.is_admin or obj.order.seller == request.user.store

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    list_display = [
        "product",
        "brand",
        "size",
        "color",
        "buyer",
        "price",
        "quantity",
        "date",
        "product_image",
    ]

    list_display_links = []

    search_fields = [
        "order__id",
    ]
