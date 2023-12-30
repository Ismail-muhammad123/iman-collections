from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Store(models.Model):
    name = models.CharField(max_length=200, unique=True)
    business_name = models.CharField(max_length=200)
    address = models.TextField()
    owener = models.OneToOneField(
        User, on_delete=models.SET_NULL, null=True, related_name="store"
    )
    email = models.EmailField()
    alternate_email = models.EmailField(null=True)
    phone_number = models.CharField(max_length=100)
    alternate_phone_number = models.CharField(max_length=100, null=True, blank=True)
    bio = models.CharField(max_length=250, null=True, blank=True)
    about = models.TextField(blank=True)
    is_registered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)

    rc_number = models.CharField(max_length=10, null=True, blank=True)
    registration_certificate = models.FileField(
        upload_to="store_verification_files/", null=True, blank=True
    )

    is_verified = models.BooleanField(default=False)
    is_open = models.BooleanField(default=False)
    last_viewed = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name