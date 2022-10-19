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

    list_filter = [
        "category",
        "gender",
        "added_by",
    ]

    exclude = ["added_by", "added_at"]

    def has_add_permission(self, request, obj=None):
        return request.user.is_admin

    def has_delete_permission(self, request, obj=None):
        return request.user.is_admin

    def has_change_permission(self, request, obj=None):
        return request.user.is_admin

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

    list_filter = [
        "added_at",
        "added_by",
    ]

    exclude = ["added_by", "added_at"]

    def save_model(self, request, obj, form, change):
        obj.added_by = request.user
        return super().save_model(request, obj, form, change)

    def has_add_permission(self, request, obj=None):
        return request.user.is_admin

    def has_delete_permission(self, request, obj=None):
        return request.user.is_admin

    def has_change_permission(self, request, obj=None):
        return request.user.is_admin


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = [
        "product",
        "quantity",
        "added_at",
        "user",
    ]

    list_filter = [
        "added_at",
    ]

    exclude = ["added_by", "added_at"]

    def has_add_permission(self, request, obj=None):
        return request.user.is_admin

    def has_delete_permission(self, request, obj=None):
        return request.user.is_admin

    def has_change_permission(self, request, obj=None):
        return request.user.is_admin
