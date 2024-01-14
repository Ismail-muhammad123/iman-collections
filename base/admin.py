from django.contrib import admin
from django.http.request import HttpRequest
from django.contrib.auth.models import Group
from rest_framework.authtoken.models import Token
from base.models import ContactMessage

from rest_framework.authtoken.models import TokenProxy

admin.site.unregister(TokenProxy)

admin.site.unregister(Group)
# admin.site.unregister(Token)


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

    list_filter = [
        "recieved_at",
    ]

    search_fields = ["email", "full_name"]

    def has_module_permission(self, request: HttpRequest, obj=None) -> bool:
        return request.user.is_admin

    def has_view_permission(self, request, obj=None):
        return request.user.is_admin

    def has_add_permission(self, request, obj=None):
        return request.user.is_admin

    def has_delete_permission(self, request, obj=None):
        return request.user.is_admin

    def has_change_permission(self, request, obj=None):
        return request.user.is_admin
