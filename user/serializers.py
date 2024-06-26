from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()


class AccountSerializer(serializers.ModelSerializer):
    gender = serializers.CharField(source="get_gender_display")

    def get_gender_display(self, obj):
        return obj.get_gender_display()

    class Meta:
        model = User
        read_only_fields = ("is_active", "is_staff", "email", "is_seller")
        fields = [
            "email",
            "first_name",
            "last_name",
            "mobile_number",
            "gender",
            "address",
            "added_at",
            "is_seller",
        ]
