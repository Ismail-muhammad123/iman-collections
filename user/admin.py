from django.contrib import admin
from .models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "email",
        "phone_number",
        "state",
        "country",
        "directions",
        "date_created",
        "profile_picture",
        "is_active",
        "is_staff",
    ]
