from django.contrib import admin
from django.urls import path, include
from products import views

urlpatterns = [
    path('', include('base.urls')),
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),

    path('api/v1/', include('api.urls')),
]
