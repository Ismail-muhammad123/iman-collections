from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField()

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
        ("U", "Unisex")
    ]

    brand_name = models.CharField(max_length=200, blank=True, default="")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    size = models.CharField(max_length=50, null=True, blank=True, default="")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, related_name="products")
    name = models.CharField(max_length=30)
    price = models.FloatField()
    available_quantity = models.PositiveIntegerField()
    delivery_days = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField()


class Saved(models.Model):
    pass
