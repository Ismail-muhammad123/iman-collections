from rest_framework import serializers
from .models import Enquiry


class EnquirySerializer(serializers.ModelSerializer):

    status = serializers.CharField(source="get_status_display")

    def get_status_display(self, obj):
        return obj.get_status_display()

    class Meta:
        model = Enquiry
        fields = [
            "name",
            "description",
            "user",
            "date_added",
            "date_found",
            "status",
        ]
