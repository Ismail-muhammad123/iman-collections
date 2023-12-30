from unicodedata import category
from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "image",
        ]


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = [
            "id",
            "name",
            "category",
            "image",
        ]


class ProductSerializer(serializers.ModelSerializer):
    gender = serializers.CharField(source="get_gender_display")
    # category = serializers.CharField(source='category__name')

    def get_gender_display(self, obj):
        return obj.get_gender_display()

    category = CategorySerializer()

    class Meta:
        model = Product
        fields = [
            "id",
            "gender",
            "category",
            "name",
            "price",
            "delivery_days",
            "description",
            "image",
        ]
