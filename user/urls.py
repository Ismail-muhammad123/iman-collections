from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('', views.login),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('logout', views.user_logout, name='logout'),
    path('resetPassword/', views.reset_password, name='reset_password'),
    path('update_password/', views.update_password, name='update_password'),

    path('password-reset/',
         views.password_reset_request, name='password_reset'),

    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='user/password_reset_mail_sent.html'
         ), name='password_reset_done'),


    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='user/password_reset_confirmation.html'
         ), name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='user/password_reset_completed.html'
         ), name='password_reset_complete')
]
