from django.db import models


class Suplier(models.Model):
    SUPPLIE_TYPE_CHOICES = [
        ("T", "Tailor"),
        ("S", "Seller"),
    ]

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    type = models.CharField(max_length=5, choices=SUPPLIE_TYPE_CHOICES)
    total_earnings = models.FloatField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()


class Product(models.Model):
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female")
    ]

    CATEGORY_CHOICES = [
        ("TD", "Tailored"),
        ("SH", "Shoes"),
        ("ST", "Shirts"),
        ("CP", "Caps"),
        ("TR", "trousers"),
        ("OTH", "Others")
    ]

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=30)
    price = models.FloatField()
    sizes = models.CharField(max_length=300)
    delivery_days = models.DurationField()
    available_quantity = models.PositiveIntegerField()
    quantity_sold = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField()
    brand_name = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name
