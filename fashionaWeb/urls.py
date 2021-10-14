from django.contrib import admin
from django.urls import path, include
from products import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include("products.urls")),
    path('cart/', include('cart.urls')),
    path('', views.home),
    path('order/', include('order.urls'))
]
