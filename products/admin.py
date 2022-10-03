from django.contrib import admin
from .models import Cart,  Product, Category
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "category",
        "gender",
        "description",
        "price",
        "product_size",
        "product_color",
        "available_quantity",
        "delivery_days",
        "image",
        "added_by"
    ]

    exclude = ["added_by", "added_at"]

    def save_model(self, request, obj, form, change):
        obj.added_by = request.user
        return super().save_model(request, obj, form, change)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "added_at",
        "added_by"
    ]

    exclude = ["added_by", "added_at"]

    def save_model(self, request, obj, form, change):
        obj.added_by = request.user
        return super().save_model(request, obj, form, change)


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = [
        "product",
        "quantity",
        "added_at",
        "user",
    ]

    exclude = ["added_by", "added_at"]
