from django.contrib import admin
from .models import Product, Category
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "gender",
        "available_quantity",
        "category",
        "description",
        "price",
        "delivery_days",
        "image",
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]
