from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('', views.login),
    path('register/', views.register, name='register'),
    path('logout', views.user_logout, name='logout'),
    path('resetPassword/', views.reset_password, name='reset_password')
]
