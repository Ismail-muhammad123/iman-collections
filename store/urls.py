from django.urls import path
from .views import *


urlpatterns = [
    path("<int:store_id>", store_products, name="store_products_page"),
    path("new", create_store, name="create_new_store"),
]
