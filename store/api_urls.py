from django.urls import path
from .api_views import *

# from rest_framework.authtoken import views
from . import views

urlpatterns = [
    path("details", StoreDetails.as_view()),
    path("create", CreateStoreAPI.as_view()),
]
