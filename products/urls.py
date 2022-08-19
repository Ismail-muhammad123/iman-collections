from django.urls import path
from . import views
from .apis import ListProducts, CategoryList, ProductCategoryList


urlpatterns = [
    # REST API
    path('list', ListProducts.as_view(), name='products_list'),
    path('categories', CategoryList.as_view(), name='categories_list'),
    path('<int:cat>', ProductCategoryList.as_view(),
         name='product_category_list'),

    # Browser
    path('', views.products, name="products"),
    path('product-details/<int:id>',
         views.product_details, name='products_details'),
    path('products-cart', views.cart, name='products_cart'),
    path('products-saved', views.saved, name='products_saved'),
    #     path('products-categories', views.category, name='categories'),
    path('products-categories/<str:category_id>',
         views.product_category, name='filter_category'),
]
