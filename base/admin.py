from django.contrib import admin

from base.models import ContactMessage

# Register your models here.


@admin.register(ContactMessage)
class ContactAdmin(admin.ModelAdmin):
    def message_content(self, obj):
        return obj.message[:10] + "..." if len(obj.message) > 10 else obj.message
    list_display = [
        "full_name",
        "email",
        "subject",
        "message_content",
        "recieved_at",
    ]

    list_filter = ["recieved_at", ]

    search_fields = ["email", "full_name"]

    def has_add_permission(self, request, obj=None):
        return request.user.is_admin

    def has_delete_permission(self, request, obj=None):
        return request.user.is_admin

    def has_change_permission(self, request, obj=None):
        return request.user.is_admin
