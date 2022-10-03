from django.contrib import admin
from django.urls import path, include
from products import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('base.urls')),
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('checout/', include('checkout.urls')),
    path('order/', include('order.urls')),
    path('account/', include('user.urls')),

    # path('api/v1/', include('api.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
