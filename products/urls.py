from django.urls import path
from . import views
from .apis import ListProducts, CategoryList, ProductCategoryList

# urlpatterns = [
#     path("", views.products),
#     path("categories/<cat>", views.category),
#     path('tailored/', views.tailored),
#     path("fabrics/", views.fabrics),
#     path("saved/", views.saved),
#     path('detail/', views.product_detaiil),
# ]


urlpatterns =[
    path('list', ListProducts.as_view(), name='products_list'),
    path('categories', CategoryList.as_view(), name='categories_list'),
    path('<int:cat>', ProductCategoryList.as_view(), name='product_category_list'),
]