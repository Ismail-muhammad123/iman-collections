from django.urls import path
from . import views

urlpatterns = [
    path("", views.products),
    path("categories/<cat>", views.category),
    path('tailored/', views.tailored),
    path("fabrics/", views.fabrics),
    path("saved/", views.saved),
    path('detail/<id>', views.product_detaiil, name="details"),
]
