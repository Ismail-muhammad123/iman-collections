from django.contrib import admin
from .models import Cart


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = [
        "item",
        "quantity",
        "date_added",
        "size",
        "user"
    ]
