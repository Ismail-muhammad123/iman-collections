from django.db import models


# class Suplier(models.Model):
#     SUPPLIE_TYPE_CHOICES = [
#         ("T", "Tailor"),
#         ("S", "Seller"),
#     ]

#     name = models.CharField(max_length=100)
#     address = models.CharField(max_length=250)
#     type = models.CharField(max_length=5, choices=SUPPLIE_TYPE_CHOICES)
#     total_earnings = models.FloatField()
#     phone_number = models.CharField(max_length=15)
#     email = models.EmailField()


class Category(models.Model):
    name = models.CharField(max_length=200)

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
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, related_name="products")
    name = models.CharField(max_length=30)
    price = models.FloatField()
    available_quantity = models.PositiveIntegerField()
    delivery_days = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField()
