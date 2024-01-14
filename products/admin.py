from django.contrib import admin
from django.http.request import HttpRequest
from django.urls import reverse
from .models import (
    Cart,
    Product,
    Category,
    ProductImage,
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

    def has_view_permission(self, request: HttpRequest, obj=None):
        return request.user.is_admin

    def has_change_permission(self, request: HttpRequest, obj=None) -> bool:
        return request.user.is_admin

    def has_add_permission(self, request: HttpRequest, obj=None) -> bool:
        return request.user.is_admin

    def has_delete_permission(self, request: HttpRequest, obj=None) -> bool:
        return request.user.is_admin

    def has_module_permission(self, request: HttpRequest, obj=None) -> bool:
        return request.user.is_admin


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "added_at",
        "color_hex_code",
    ]

    def has_view_permission(self, request, obj=None):
        return request.user.is_admin

    def has_change_permission(self, request, obj=None) -> bool:
        return request.user.is_admin

    def has_add_permission(self, request, obj=None) -> bool:
        return request.user.is_admin

    def has_delete_permission(self, request, obj=None) -> bool:
        return request.user.is_admin

    def has_module_permission(self, request: HttpRequest, obj=None) -> bool:
        return request.user.is_admin


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
        return obj.sub_categories.count()

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

    def has_module_permission(self, request: HttpRequest, obj=None) -> bool:
        return request.user.is_admin

    def has_view_permission(self, request: HttpRequest, obj=None) -> bool:
        return request.user.is_admin

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

    def has_module_permission(self, request: HttpRequest, obj=None) -> bool:
        return request.user.is_admin

    def has_view_permission(self, request: HttpRequest, obj=None) -> bool:
        return request.user.is_admin

    def has_add_permission(self, request, obj=None):
        return request.user.is_admin

    def has_delete_permission(self, request, obj=None):
        return request.user.is_admin

    def has_change_permission(self, request, obj=None):
        return request.user.is_admin


class ProductVariantInline(admin.TabularInline):
    model = ProductVariant


class ProductImageInline(admin.TabularInline):
    model = ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    def product_images(self, obj):
        display_text = f"<img src={obj.image.url} width='100px' height='100px'/>"

        if display_text:
            return mark_safe(display_text)
        return "-"

    def variants(self, obj):
        return obj.product_variants.count()

    def seller(self, obj):
        return obj.store.name

    inlines = [
        ProductImageInline,
        ProductVariantInline,
    ]

    list_display = [
        "name",
        "category",
        "sub_category",
        "gender",
        "description",
        "on_sale",
        "delivery_days",
        "added_at",
        "is_active",
        "seller",
        # "product_images",
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

    readonly_fields = [
        "store",
        "slug",
    ]

    def create_slug(self, request, queryset):
        for obj in queryset:
            obj.save()

    def has_view_permission(self, request: HttpRequest, obj=None) -> bool:
        return request.user.is_admin or (
            request.user.is_seller and (obj and request.user.store == obj.store)
        )

    def has_add_permission(self, request: HttpRequest, obj=None):
        return request.user.is_admin or (request.user.is_seller)

    def has_delete_permission(self, request: HttpRequest, obj=None):
        return request.user.is_admin or (
            request.user.is_seller and (obj and request.user.store == obj.store)
        )

    def has_change_permission(self, request: HttpRequest, obj=None):
        return request.user.is_admin or (
            request.user.is_seller and (obj and request.user.store == obj.store)
        )

    def save_model(self, request, obj, form, change):
        obj.added_by = request.user
        if request.user.store is not None:
            obj.store = request.user.store
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
        "delivery_fee",
        "available_quantity",
        "variant_image",
    ]

    def has_view_permission(self, request: HttpRequest, obj=None) -> bool:
        return request.user.is_admin or (
            request.user.is_seller and (obj and request.user.store == obj.product.store)
        )

    def has_add_permission(self, request, obj=None):
        return request.user.is_admin or (request.user.is_seller)

    def has_delete_permission(self, request, obj=None):
        return request.user.is_admin or (
            request.user.is_seller and (obj and request.user.store == obj.product.store)
        )

    def has_change_permission(self, request, obj=None):
        return request.user.is_admin or (
            request.user.is_seller and (obj and request.user.store == obj.product.store)
        )


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
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

    def has_view_permission(self, request: HttpRequest, obj=None) -> bool:
        return request.user.is_admin or (
            request.user.is_seller and (obj and request.user.store == obj.product.store)
        )

    def has_add_permission(self, request, obj=None):
        return request.user.is_admin or (request.user.is_seller)

    def has_delete_permission(self, request, obj=None):
        return request.user.is_admin or (
            request.user.is_seller and (obj and request.user.store == obj.product.store)
        )

    def has_change_permission(self, request, obj=None):
        return request.user.is_admin or (
            request.user.is_seller and (obj and request.user.store == obj.product.store)
        )


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
            f"<img src={obj.product_variant.image.url} width='100px' height='100px'/>",
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

    def has_module_permission(self, request: HttpRequest, obj=None) -> bool:
        return request.user.is_admin

    def has_view_permission(self, request: HttpRequest, obj=None) -> bool:
        return request.user.is_admin

    def has_add_permission(self, request, obj=None):
        return request.user.is_admin

    def has_delete_permission(self, request, obj=None):
        return request.user.is_admin

    def has_change_permission(self, request, obj=None):
        return request.user.is_admin
