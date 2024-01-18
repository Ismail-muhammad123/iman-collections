from django.urls import path
from .apis import *



urlpatterns = [
    path("profile", UserDetails.as_view()),
]