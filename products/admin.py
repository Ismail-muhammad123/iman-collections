from django.contrib import admin
from .models import Color, Inventory, Product, Category, Size
# Register your models here.


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]


@admin.register(Inventory)
class InevtnoryAdmin(admin.ModelAdmin):
    list_display = [
        "product",
        "size",
        "color",
    ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "gender",
        "category",
        "description",
        "delivery_days",
        "image",
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]
