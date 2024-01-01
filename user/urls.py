from django.urls import path
from .apis import UserDetails
from . import views

urlpatterns = [
    path('logout', views.signout, name="logout"),
    path('login', views.signIn, name="login"),
    path('register', views.register, name="create_account"),
    path('profile', views.profile, name="profile"),
    path('edit-profile', views.editProfile, name="edit_profile"),
    path('reset-password', views.reset_password, name="reset_password"),

]
