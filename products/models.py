from django.db import models


class Color(models.Model):
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="product_categories")

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
    delivery_days = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to="products")

    def __str__(self) -> str:
        return self.name


class Inventory(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.DO_NOTHING, related_name="inventory")
    size = models.ForeignKey(
        Size, on_delete=models.DO_NOTHING, related_name="inventory")
    color = models.ForeignKey(
        Color, on_delete=models.DO_NOTHING, related_name="inventory")
    price = models.FloatField()
    available_quantity = models.PositiveIntegerField()
    image_one = models.ImageField(upload_to="inevntory_images")
    image_two = models.ImageField(upload_to="inevntory_images")
    image_three = models.ImageField(upload_to="inevntory_images")


class Cart(models.Model):
    product = models.ForeignKey(Inventory, on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField()
    added_at = models.DateTimeField(auto_now_add=True)
