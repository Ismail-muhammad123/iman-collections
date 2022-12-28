from django.contrib import admin
from django.urls import reverse
from .models import Cart,  Product, Category
from django.utils.safestring import mark_safe


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    def available(self, obj):
        return obj.available_quantity

    def delivery(self, obj):
        return obj.delivery_days

    def size(self, obj):
        return obj.product_size

    def color(self, obj):
        return obj.product_color

    def by(self, obj):
        return obj.added_by.first_name

    list_display = [
        "name",
        "category",
        "gender",
        "description",
        "price",
        "size",
        "color",
        "available",
        "delivery",
        "added_at",
        "is_active",
        "by",
        "product_image",
    ]

    list_filter = [
        "category",
        "gender",
        "is_active",
        "added_by",
    ]

    exclude = ["added_by", "added_at"]

    actions = [
        "create_slug",
    ]

    search_fields = ["id"]

    def product_image(self, obj):
        display_text = "<a href={}>{}</a>".format(
            obj.image.url, f"<img src={obj.image.url} width='100px' height='100px'/>")

        if display_text:
            return mark_safe(display_text)
        return "-"

    def create_slug(modeladmin, request, queryset):
        for obj in queryset:
            obj.save()

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
    def category_image(self, obj):
        display_text = "<a href={}>{}</a>".format(
            obj.image.url,
            f"<img src={obj.image.url} width='100px' height='100px'/>")

        if display_text:
            return mark_safe(display_text)
        return "-"

    def number_of_products(self, obj):
        return obj.products.count()

    list_display = [
        "name",
        "number_of_products",
        "added_at",
        "added_by",
        "category_image",
    ]

    list_filter = [
        "added_at",
        "added_by",
    ]

    exclude = ["added_by", "added_at"]

    actions = [
        "create_slug",
    ]

    def create_slug(modeladmin, request, queryset):
        for obj in queryset:
            obj.save()

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
    def product_image(self, obj):
        display_text = "<a href={}>{}</a>".format(
            reverse('admin:{}_{}_changelist'.format(Product._meta.app_label, Product._meta.model_name),
                    ) + f"?q={obj.product.pk}",
            f"<img src={obj.product.image.url} width='100px' height='100px'/>")

        if display_text:
            return mark_safe(display_text)
        return "-"

    list_display = [
        "product",
        "quantity",
        "added_at",
        "user",
        "product_image",
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
