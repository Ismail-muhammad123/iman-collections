from django.urls import path
from .views import *


urlpatterns = [
    path("<int:store_id>", store_products, name="store_products_page"),
    path("new", create_store, name="create_new_store"),
    # path("plan", update_plan, name="update_store_plan"),
    path("profile", view_store_profile, name="view_store_profile"),
]
