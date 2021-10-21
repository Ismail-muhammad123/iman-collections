from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout),
    path('success/', views.success),
    path('canceled/', views.canceled),
    path('initialize/', views.initialize, name='initialize_payment')
]
