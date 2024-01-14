from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime, timedelta

User = get_user_model()


class Plan(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Subscription(models.Model):
    STATUS_CHOICES = [
        (0, "Inactive"),
        (1, "Active"),
    ]

    plan = models.ForeignKey(
        Plan, on_delete=models.SET_NULL, null=True, related_name="subscriptions"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    store = models.OneToOneField(
        "Store", on_delete=models.SET_NULL, null=True, related_name="subscription"
    )
    subscription_code = models.CharField(max_length=200, null=True, blank=True)
    status = models.PositiveIntegerField(choices=STATUS_CHOICES, default=0)
    canceled_at = models.DateTimeField(null=True, blank=True)

    expires_at = models.DateField(null=True, blank=True)

    def has_expired(self):
        return (self.expires_at - datetime.now()).days > 0

    


class SubscriptionPayment(models.Model):
    STATUS_CHOICES = [
        (0, "Failed"),
        (1, "Pending"),
        (2, "Success"),
    ]

    # fields
    subscription = models.ForeignKey(
        Subscription, on_delete=models.SET_NULL, null=True, related_name="payments"
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    store = models.ForeignKey(
        "Store",
        on_delete=models.SET_NULL,
        null=True,
        related_name="subscription_payments",
    )
    added_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES)


class Store(models.Model):
    business_name = models.CharField(max_length=200, blank=True, null=True)
    business_address = models.TextField()
    owner = models.OneToOneField(
        User, on_delete=models.SET_NULL, null=True, related_name="store"
    )
    email = models.EmailField()
    alternate_email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=100)
    alternate_phone_number = models.CharField(max_length=100, null=True, blank=True)
    about = models.TextField(blank=True)
    display_picture = models.ImageField(
        upload_to="display_pictures/", null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now=True)

    # Business registration info
    is_registered = models.BooleanField(default=False)
    tin = models.CharField(max_length=200, blank=True, null=True)
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
        return self.business_name

    def trial_expired(self):
        return (datetime.now() - self.created_at).days >= 14

    def is_subscribed(self):
        return self.subscription is not None and self.subscription.is_active


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
