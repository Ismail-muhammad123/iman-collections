from rest_framework import serializers

from products.serializers import ProductSerializer
from .models import Order


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        read_only_fields = ["status", ]
        fields = [
            "product",
            "quantity",
            "total_amount",
            "tracking_id",
            "payment",
            "delivery_date",
            "status",
            "date_added",
        ]
