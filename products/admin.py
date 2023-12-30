from django.contrib import admin
from django.urls import reverse
from .models import (
    Cart,
    Product,
    Category,
    ProductImages,
    ProductVariant,
    Size,
    Color,
    SubCategory,
)
from django.utils.safestring import mark_safe


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "added_at",
        "added_by",
    ]


@admin.register(Color)
class SizeAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "added_at",
        "color_hex_code",
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    def category_image(self, obj):
        display_text = "<a href={}>{}</a>".format(
            obj.image.url, f"<img src={obj.image.url} width='100px' height='100px'/>"
        )

        if display_text:
            return mark_safe(display_text)
        return "-"

    def number_of_products(self, obj):
        return obj.products.count()

    def subcategories(self, obj):
        return obj.sub_categories.cout()

    list_display = [
        "name",
        "number_of_products",
        "subcategories",
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


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    def sub_category_image(self, obj):
        display_text = "<a href={}>{}</a>".format(
            obj.image.url, f"<img src={obj.image.url} width='100px' height='100px'/>"
        )

        if display_text:
            return mark_safe(display_text)
        return "-"

    def number_of_products(self, obj):
        return obj.products.count()

    list_display = [
        "name",
        "category",
        "number_of_products",
        "added_at",
        "added_by",
        "sub_category_image",
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


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    def variants(self, obj):
        return obj.product_variants.count()

    def seller(self, obj):
        return obj.store.name

    list_display = [
        "name",
        "category",
        "sub_category",
        "gender",
        "description",
        "on_sale",
        "available_quantity",
        "delivery_days",
        "added_at",
        "is_active",
        "seller",
        "images",
    ]

    list_filter = [
        "category",
        "sub_category",
        "gender",
        "is_active",
        "added_by",
        "added_at",
        "on_sale",
    ]

    exclude = ["added_by", "added_at"]

    actions = [
        "create_slug",
    ]

    search_fields = ["id"]

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


@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    def variant_image(self, obj):
        display_text = "<a href={}>{}</a>".format(
            obj.image.url, f"<img src={obj.image.url} width='100px' height='100px'/>"
        )

        if display_text:
            return mark_safe(display_text)
        return "-"

    list_display = [
        "product",
        "size",
        "color",
        "price",
        "available_quantity",
        "variant_image",
    ]


@admin.register(ProductImages)
class ProductImagesAdmin(admin.modelAdmin):
    def product_image(self, obj):
        display_text = "<a href={}>{}</a>".format(
            obj.image.url, f"<img src={obj.image.url} width='100px' height='100px'/>"
        )

        if display_text:
            return mark_safe(display_text)
        return "-"

    list_display = [
        "product",
        "product_image",
    ]


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    def product_variant_image(self, obj):
        display_text = "<a href={}>{}</a>".format(
            reverse(
                "admin:{}_{}_changelist".format(
                    ProductVariant._meta.app_label, ProductVariant._meta.model_name
                ),
            )
            + f"?q={obj.pk}",
            f"<img src={obj.image.url} width='100px' height='100px'/>",
        )

        if display_text:
            return mark_safe(display_text)
        return "-"

    list_display = [
        "product_variant",
        "quantity",
        "added_at",
        "user",
        "device",
        "product_variant_image",
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
