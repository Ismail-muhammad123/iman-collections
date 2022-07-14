from django.contrib import admin
from .models import Enquiry


@admin.register(Enquiry)
class EnquaryAdmin(admin.ModelAdmin):

    list_display = [
        "name",
        "description",
        "user",
        "date_added",
        "date_found",
        "status",
    ]