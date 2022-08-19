from django.urls import path
from .apis import OrderList, OrderDetails, CreateOrderAPIView
from . import views

urlpatterns = [
    path('list', OrderList.as_view()),
    path('details/<int:id>', OrderDetails.as_view()),
    path('create', CreateOrderAPIView.as_view()),

    path("my-order", views.order, name="track_order")
]
