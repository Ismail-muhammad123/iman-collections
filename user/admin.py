from django.contrib import admin
from django.contrib.auth import get_user_model


User = get_user_model()


admin.site.site_header = "Iman Clothing and Apparels"
admin.site.site_title = "Iman Clothing | Admin"
admin.site.index_title = "Dashboard"


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    list_display = [
        "email",
        "first_name",
        "last_name",
        "mobile_number",
        "gender",
        "added_at",
        "staff",
        "admin",
        "is_active",
    ]

    list_filter = [
        "is_active",
        "gender",
        "staff",
        "admin"
    ]

    search_fields = [
        "email",
        "first_name",
        "last_name",
        "mobile_number"
    ]
