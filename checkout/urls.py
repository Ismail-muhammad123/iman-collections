from django.urls import path
from . import views

urlpatterns = [
    path('pay', views.checkout, name="order_checkout"),
    path('verify', views.verify_payment, name="verify_checkout"),
]
