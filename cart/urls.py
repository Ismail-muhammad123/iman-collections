from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('remove/', views.remove, name='remove_cart'),
    path('clear/', views.clear)
]
