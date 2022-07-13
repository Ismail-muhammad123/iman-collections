from django.urls import path, include


urlpatterns =[
    path('products/', include('products.urls')),
    path('cart/', include('cart.urls')),
    path('account/', include('user.urls')),
    path('order/', include('order.urls')),

]