from secrets import choice
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Enquiry(models.Model):

    STATUS_CHOICES = [
        ("F", "Found"),
        ("N", "Not Found"),
        ("P", "Pending"),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="enquiries")
    date_added = models.DateTimeField(auto_now_add=True)
    date_found = models.DateField(null=True)
    status = models.CharField(
        max_length=1, choices=STATUS_CHOICES, default="P")
