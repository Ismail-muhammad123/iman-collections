from django.contrib import admin
from django.urls import path, include
from products import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500
from base import views as base_views


urlpatterns = [
    path('', include('base.urls')),
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('checkout/', include('checkout.urls')),
    path('order/', include('order.urls')),
    path('account/', include('user.urls')),

    # path('api/v1/', include('api.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


handler404 = base_views.error_404
handler500 = base_views.error_500
