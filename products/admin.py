from django.contrib import admin
from .models import Message, Product, Category, SavedProducts, Suplier


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone_number",
                    "subject", "message", "sent_at"]
    search_fields = ["name", "phone_number"]


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
        "supplier",
        "suplier_paid",
        "image",
        "added_by",
        "added_at"
    ]

    exclude = ['added_by']

    def save_model(self, request, obj, form, change):
        obj.added_by = request.user
        super(ProductAdmin, self).save_model(request, obj, form, change)

    def make_suplier_paid(modeladmin, request, queryset):
        queryset.update(suplier_paid=True)

    def make_suplier_not_paid(modeladmin, request, queryset):
        queryset.update(suplier_paid=False)

    actions = [make_suplier_not_paid, make_suplier_paid]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "gender",
        "image",
        "added_at",
        "added_by"
    ]

    exclude = ['added_by']

    def save_model(self, request, obj, form, change):
        obj.added_by = request.user
        super(CategoryAdmin, self).save_model(request, obj, form, change)


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

    exclude = ['added_by']

    def save_model(self, request, obj, form, change):
        obj.added_by = request.user
        super(SuplierAdmin, self).save_model(request, obj, form, change)


@admin.register(SavedProducts)
class SavedProductsAdmin(admin.ModelAdmin):
    list_display = [
        "item",
        "date_added",
        "user"
    ]


admin.site.site_title = "Fashiona Dashboard"
admin.site.site_header = "Fashiona Collections Admin Dashboard"
admin.site.index_title = "Fashiona Dashboard"
