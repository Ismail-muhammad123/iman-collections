from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login),
    path('', views.login),
    path('register/', views.register),
    path('resetPassword/', views.reset_password)
]
