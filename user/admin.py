from django.contrib import admin
from django.contrib.auth import get_user_model


User = get_user_model()
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    list_display = [
        "email",
        "first_name",
        "last_name",
        "mobile_number",
        "gender",
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
