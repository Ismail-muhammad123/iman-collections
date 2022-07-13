from rest_framework import serializers
from .models import Cart
from products.serializers import ProductSerializer


class CartSerializer(serializers.ModelSerializer):
    # item = ProductSerializer()

    class Meta:
        model = Cart
        fields = [
            "item",
            "quentity",
            "date_added"
        ]
