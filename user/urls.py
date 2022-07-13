from django.urls import path
from .apis import UserDetails
from rest_framework.authtoken import views

urlpatterns = [
    # path('login/', views.login),
    # path('', views.login),
    # path('register/', views.register),
    # path('resetPassword/', views.reset_password)

    path('login', views.obtain_auth_token),
    path('details', UserDetails.as_view()),

]
