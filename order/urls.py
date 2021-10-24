from django.urls import path
from . import views

urlpatterns = [
    path('', views.order),
    path('details/<order_id>', views.order_detail, name="order_details"),
]
