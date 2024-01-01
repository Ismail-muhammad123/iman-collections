from rest_framework.views import APIView
from rest_framework import permissions, status
from products.models import ProductVariant
from .serializers import StoreSerializer
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from products.models import ProductVariant, Product, ProductImage
from products.serializers import ProductSerializer, ProductVariantSerializer

User = get_user_model()


# ============================ STORE ============================
# RETRIVE and UPDATE STORE
class StoreDetails(APIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get(self, request):
        store = request.user.store
        if store is not None:
            serializer = StoreSerializer(instance=store)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        data = request.data
        files = request.FILES

        store = request.user.store
        if store is not None:
            serializer = StoreSerializer(instance=store, data=data, files=files)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer, status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


# CREATE STORE
class CreateStoreAPI(APIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def post(self, request):
        data = request.data
        files = request.FILES

        store = request.user.store
        if store is None:
            user: User = request.user
            user.is_seller = True
            user.save()
            serializer = StoreSerializer(data=data, files=files)
            if serializer.is_valid():
                serializer.create(serializer.validated_data)
                return Response(serializer, status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)


# DELETE Store
class CloseStore(APIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def post(self, request, id):
        store = request.user.store

        if store is not None:
            store.is_open = False
            store.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


# ============================ PRODUCT ============================
# LIST products
class ListProducts(APIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get(self, request):
        store = request.user.store
        if store is not None:
            products = store.products.get()
            serializer = ProductSerializer(instance=products, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


# CREATE PRODUCT
class CreateProduct(APIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def post(self, request):
        store = request.user.store
        if store is not None:
            serializer = ProductSerializer(data=request.data, files=request.FILES)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


# UPDATE, DELETE product
class ProductDetails(APIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def post(self, request, id):
        store = request.user.store
        if store is not None:
            product = store.products.get(id=id)
            if product is not None:
                serializer = ProductSerializer(
                    instance=product, data=request.data, files=request.FILES
                )
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, id):
        store = request.user.store
        if store is not None:
            product: Product = store.products.get(id=id)
            if product is not None:
                product.active = False
                product.save()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


# ============================ PRODUCT VARIANT ============================
# LIST Product variants
class ListProductVariants(APIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get(self, request, product_id):
        store = request.user.store
        if store is not None:
            product = store.products.get(id=product_id)
            if product is not None:
                variants = product.product_variants.get()
                serializer = ProductVariantSerializer(instance=variants, many=True)
                return Response(serializer.data)
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


# CREATE new Product Variant
class CreateProductVariant(APIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def post(self, request, product_id):
        store = request.user.store

        if store is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        product = Product.object.get(pk=product_id)

        if product.store == store:
            serializer = ProductVariantSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


# UPDATE DELETE product variant
class ProductVariantDetails(APIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def post(self, request, product_id, variant_id):
        product = Product.objects.get(pk=product_id)
        variant = ProductVariant.objects.get(pk=variant_id)
        store = request.user.store
        if store is not None and variant.product == product and product.store == store:
            serializer = ProductVariantSerializer(instance=variant, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, product_id, variant_id):
        product = Product.objects.get(pk=product_id)
        variant = ProductVariant.objects.get(pk=variant_id)
        store = request.user.store
        if store is not None and variant.product == product and product.store == store:
            variant.active = False
            variant.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


# ============================ ORDERS ============================


# ============================ PAYMENTS ============================
