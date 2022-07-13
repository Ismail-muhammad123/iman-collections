from django.urls import path
from .apis import OrderList, OrderDetails, CreateOrderAPIView

urlpatterns = [
    path('list', OrderList.as_view()),
    path('details/<int:id>', OrderDetails.as_view()),
    path('create', CreateOrderAPIView.as_view()),
]
