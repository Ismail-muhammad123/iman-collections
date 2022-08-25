from django.urls import path
from . import views
from .apis import ListProducts, CategoryList, ProductCategoryList


urlpatterns = [
    # REST API
    #     path('list', ListProducts.as_view(), name='products_list'),
    #     path('categories', CategoryList.as_view(), name='categories_list'),
    #     path('<int:cat>', ProductCategoryList.as_view(),
    #          name='product_category_list'),


    path('categories', views.categories, name='categories'),
    path('categories/<int:category_id>',
         views.product_category, name='filter_category'),
    path('', views.products, name="products"),
    path('search', views.search, name="search_product"),
    path('<int:id>',
         views.product_details, name='products_details'),
]
