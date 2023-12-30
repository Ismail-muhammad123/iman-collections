from django.contrib import admin

from store.models import Store

# Register your models here.


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display =[
        "name",
        "business_name",
        "address",
        "owener",
        "email",
        "alternate_email",
        "phone_number",
        "alternate_phone_number",
        "bio",
        "about",
        "is_registered",
        "created_at",
        "rc_number",
        "registration_certificate",
        "is_verified",
        "is_open",
        "last_viewed",
    ]