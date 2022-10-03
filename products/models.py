from email.policy import default
from django.db import models


class Size(models.Model):
    name = models.CharField(max_length=100)
    added_at = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(
        "user.User", on_delete=models.DO_NOTHING, related_name="sizes_added")

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="categories", blank=True)
    added_at = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(
        "user.User", on_delete=models.DO_NOTHING, related_name="categories_added")

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
    product_size = models.CharField(max_length=200, blank=True, default="")
    product_color = models.CharField(max_length=200, blank=True, default="")
    available_quantity = models.PositiveBigIntegerField()
    delivery_days = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to="product-images", blank=True)

    added_at = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(
        "user.User", on_delete=models.DO_NOTHING, related_name="products_added")

    def __str__(self) -> str:
        return self.name


# class Inventory(models.Model):
#     name = models.CharField(max_length=200, blank=True)
#     product = models.ForeignKey(
#         Product, on_delete=models.DO_NOTHING, related_name="inventory")
#     size = models.ForeignKey(
#         Size, on_delete=models.DO_NOTHING, related_name="inventory")
#     color = models.ForeignKey(
#         Color, on_delete=models.DO_NOTHING, related_name="inventory")
#     price = models.FloatField()
#     available_quantity = models.PositiveIntegerField()
#     # images = models.ManyToManyField(
#     #     Image, related_name="inevntory_images")

#     added_at = models.DateTimeField(auto_now_add=True)
#     added_by = models.ForeignKey(
#         "user.User", on_delete=models.DO_NOTHING, related_name="inventory_added")


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField()
    added_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        "user.User", on_delete=models.DO_NOTHING, related_name="cart")

    class Meta:
        verbose_name_plural = "Cart"
