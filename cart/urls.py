from django.urls import path
from . import views
from .apis import CartList, CartSingle

urlpatterns = [
    path('list', CartList.as_view(), name="list_cart_items"),
    path('single', CartSingle.as_view(), name="insert_cart_item"),
]
