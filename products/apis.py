from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from products.serializers import ProductSerializer, CategorySerializer
from .models import Category, Product


class ListProducts(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        products = Product.objects.all()

        serializer = ProductSerializer(instance=products, many=True)
        return Response(serializer.data)


class CategoryList(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        categories = Category.objects.all()

        serializer = CategorySerializer(instance=categories, many=True)

        return Response(serializer.data)


class ProductCategoryList(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, cat):
        print(cat)
        category = Category.objects.get(id=cat)
        product = category.products.all()
        serializer = ProductSerializer(instance=product, many=True)

        return Response(serializer.data)