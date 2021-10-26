from django.db import models


class Category(models.Model):

    GENDER_CHOICES = [
        ("U", "Unisex"),
        ("M", "Male"),
        ("F", "Female")
    ]

    name = models.CharField(max_length=50)
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, default="U")
    image = models.ImageField(upload_to='CategoriesImages')
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


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

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    product_category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=30)
    price = models.FloatField()
    size = models.CharField(max_length=300)
    delivery_in = models.PositiveIntegerField()
    available_quantity = models.PositiveIntegerField()
    quantity_sold = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='productImages')
    brand_name = models.CharField(max_length=250)
    color = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name
