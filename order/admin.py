from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "date_added",
        "total_amount",
        "delivery_date",
        "status",
    ]
