from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from products import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include("products.urls")),
    path('cart/', include('cart.urls')),
    path('', views.home),
    path('contact/', views.contact),
    path('order/', include('order.urls')),
    path('payment/', include('payment.urls')),
    path('user/', include('user.urls')),
    path('favicon.ico', RedirectView.as_view(
        url=staticfiles_storage.url('home/favicon.ico')))

]


handler404 = 'products.views.error_404'
handler500 = 'products.views.error_500'
