from django.contrib import admin
from .models import Product, Category, SavedProducts, Suplier


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "price",
        "size",
        "product_category",
        "available_quantity",
        "quantity_sold",
        "color",
        "brand_name",
        "gender",
        "description",
        "image",
        "added_by",
        "added_at"
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "gender",
        "image",
        "added_at",
        "added_by"
    ]


@admin.register(Suplier)
class SuplierAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "state",
        "country",
        "address",
        "phone_number",
        "email",
        "added_by",
        "added_at"
    ]


@admin.register(SavedProducts)
class SavedProductsAdmin(admin.ModelAdmin):
    list_display = [
        "item",
        "date_added",
        "user"
    ]
