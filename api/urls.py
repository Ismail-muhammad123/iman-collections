from django.urls import path, include
from rest_framework.authtoken import views


urlpatterns = [
    # path("products/", include("products.urls")),
    # path("cart/", include("cart.urls")),
    # path("account/", include("user.urls")),
    # path("order/", include("order.urls")),
    # path("enquaries/", include("enquaries.urls")),
    path("store/", include("store.api_urls")),
    path("account/", include("user.api_urls")),
    path("login", views.obtain_auth_token),
]
