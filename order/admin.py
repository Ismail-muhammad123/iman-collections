from django.contrib import admin
from django.urls import reverse
from .models import Order, OrderItem
from django.utils.safestring import mark_safe
from checkout.models import Payment


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    def name(self, obj):
        return obj.user.first_name + " " + obj.user.last_name

    def payment_status(self, obj):
        display_text = "<a href={}>{}</a>".format(
            reverse('admin:{}_{}_changelist'.format(Payment._meta.app_label, Payment._meta.model_name),
                    ) + f"?q={obj.pk}",
            obj.payment.get_status_display())

        if display_text:
            return mark_safe(display_text)
        return "-"

    def items(self, obj):
        display_text = "<a href={}>{}</a>".format(
            reverse('admin:{}_{}_changelist'.format(OrderItem._meta.app_label, OrderItem._meta.model_name),
                    ) + f"?q={obj.pk}",
            f"View Items")

        if display_text:
            return mark_safe(display_text)
        return "-"

    list_display = [
        "id",
        "name",
        "items",
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

    list_filter = [
        "status",
        "delivery_date",
        "date_added"
    ]

    def has_add_permission(self, request, obj=None):
        return request.user.is_admin

    def has_delete_permission(self, request, obj=None):
        return request.user.is_admin

    def has_change_permission(self, request, obj=None):
        return request.user.is_admin


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    def buyer(self, obj):
        return obj.order.user.first_name + " " + obj.order.user.last_name

    def date(self, obj):
        return obj.order.date_added

    def price(self, obj):
        return obj.product.price

    def brand(self, obj):
        return obj.product.brand_name

    def size(self, obj):
        return obj.product.product_size

    def color(self, obj):
        return obj.product.product_color

    def has_add_permission(self, request, obj=None):
        return request.user.is_admin

    def has_delete_permission(self, request, obj=None):
        return request.user.is_admin

    def has_change_permission(self, request, obj=None):
        return request.user.is_admin
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
    ]

    list_display_links = []

    search_fields = [
        "order__id",
    ]
