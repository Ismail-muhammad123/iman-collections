from rest_framework import serializers
from .models import Payout, Store

# from django.contrib.auth import get_user_model
# User = get_user_model()


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        read_only_fields = (
            "is_active",
            "created_at",
            "last_viewed",
            "owener",
            "is_verified",
        )
        fields = [
            "name",
            "business_name",
            "address",
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


class PayoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payout
        fields = [
            "currency",
            "amount",
            "store",
            "bank_name",
            "account_name",
            "account_number",
            "time",
            "added_by",
        ]
