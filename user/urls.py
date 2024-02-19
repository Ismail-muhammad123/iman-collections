from django.urls import path
from .apis import UserDetails
from . import views

urlpatterns = [
    path("logout", views.signout, name="logout"),
    path("login", views.signIn, name="login"),
    path("register", views.register, name="create_account"),
    path("profile", views.profile, name="profile"),
    path("edit-profile", views.editProfile, name="edit_profile"),
    path(
        "verify-account/<str:id>/<str:token>",
        views.verify_account,
        name="verify_account_page",
    ),
    path("forget-password", views.forget_password, name="reset_password"),
    path(
        "set_new_password/<str:id>/<str:token>", views.new_password, name="new_password"
    ),
]
