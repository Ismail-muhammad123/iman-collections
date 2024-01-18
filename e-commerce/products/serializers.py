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


class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = [
            "id",
            "product",
            "size",
            "color",
            "price",
            "available_quantity",
            "delivery_fee",
            "image",
        ]


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        mode = ProductImage
        fields = [
            "id",
            "product",
            "image",
        ]


class ProductSerializer(serializers.ModelSerializer):
    gender = serializers.CharField(source="get_gender_display")
    # category = serializers.CharField(source='category__name')

    def get_gender_display(self, obj):
        return obj.get_gender_display()

    category = CategorySerializer()

    sub_category = SubCategorySerializer()

    variants = ProductVariantSerializer(many=True)

    images = ProductImageSerializer(many=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "gender",
            "category",
            "sub_category",
            "variants",
            "name",
            "price",
            "delivery_days",
            "description",
            "images",
        ]
