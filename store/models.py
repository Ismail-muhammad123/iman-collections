from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Store(models.Model):
    name = models.CharField(max_length=200, unique=True)
    business_name = models.CharField(max_length=200, blank=True, null=True)
    address = models.TextField()
    owner = models.OneToOneField(
        User, on_delete=models.SET_NULL, null=True, related_name="store"
    )
    email = models.EmailField()
    alternate_email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=100)
    alternate_phone_number = models.CharField(max_length=100, null=True, blank=True)
    bio = models.CharField(max_length=250, null=True, blank=True)
    about = models.TextField(blank=True)
    is_registered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)

    # bank registration info
    rc_number = models.CharField(max_length=10, null=True, blank=True)
    registration_certificate = models.FileField(
        upload_to="store_verification_files/", null=True, blank=True
    )

    # bank account info
    bank_name = models.CharField(max_length=100, blank=True, null=True)
    account_name = models.CharField(max_length=200, blank=True, null=True)
    account_number = models.CharField(max_length=200, blank=True, null=True)
    bvn = models.CharField(max_length=200, blank=True, null=True)

    # Store State
    is_verified = models.BooleanField(default=False)
    is_open = models.BooleanField(default=False)
    last_viewed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Payout(models.Model):
    CURRENCY_CHOICES = [
        ("ngn", "Nigerian Naira"),
        ("usd", "US Dollar"),
    ]
    currency = models.CharField(max_length=5, choices=CURRENCY_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    store = models.ForeignKey(
        Store, on_delete=models.SET_NULL, null=True, related_name="payouts"
    )

    bank_name = models.CharField(max_length=100, blank=True, null=True)
    account_name = models.CharField(max_length=200, blank=True, null=True)
    account_number = models.CharField(max_length=200, blank=True, null=True)

    time = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="payouts",
        limit_choices_to={"admin": True},
    )
