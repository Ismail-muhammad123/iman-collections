from django.urls import path
from .api_views import *

# from rest_framework.authtoken import views
from . import views

urlpatterns = [
    path("details", StoreDetails.as_view()),
    path("create", CreateStoreAPI.as_view()),
    path("close", CloseStore.as_view()),
    # PRODUCTS
    path("products", ListProducts.as_view()),
    path("products/new", CreateProduct.as_view()),
    path("products/details/<id>", ProductDetails.as_view()),
    # PRODUCT VARIETY
    path("products/<product_id>/variants", ListProductVariants.as_view()),
    path("products/<product_id>/variants/new", CreateProductVariant.as_view()),
    path(
        "products/<product_id>/variants/<variant_id>/details",
        ProductVariantDetails.as_view(),
    ),
]
