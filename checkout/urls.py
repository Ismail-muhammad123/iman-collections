from django.urls import path
from . import views

urlpatterns = [
    path('pay/<int:order_id>', views.checkout, name="order_checkout"),
    path('verify', views.verify_payment, name="verify_checkout"),
]
