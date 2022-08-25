from django.urls import path
from .apis import OrderList, OrderDetails, CreateOrderAPIView
from . import views

urlpatterns = [
    # path('list', OrderList.as_view()),
    # path('details/<int:id>', OrderDetails.as_view()),
    # path('create', CreateOrderAPIView.as_view()),

    path("new-order", views.new_order, name="new_order"),
    path("track-order", views.my_order, name="my_order"),
    path("track-order/<str:tracking_id>", views.track_order, name="track_order")
]
