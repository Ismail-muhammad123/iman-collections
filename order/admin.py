from django.contrib import admin
from .models import Order, OrderProduct


class OrderProductAdmin(admin.ModelAdmin):
    class Meta:
        field = ["__all__"]


admin.site.register(Order)
admin.site.register(OrderProduct, OrderProductAdmin)
