from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("saved/new", views.save_item, name="save_new"),
    path("saved/remove", views.remove_saved, name="remove_saved"),
    # path("categories/<category>", views.category, name="category"),
    path('g/<gender>/', views.gender, name="gender"),
    path("categories/<gender>/<category>",
         views.category_gender, name="gender_category"),
    path("saved/", views.saved),
    path('detail/<id>', views.product_detaiil, name="details"),
    path('search/', views.search, name="search"),

]
