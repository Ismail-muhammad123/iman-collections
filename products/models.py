from django.db import models
from django.conf import settings


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

    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.name + ' - ' + self.get_gender_display()


class Suplier(models.Model):
    SUPPLIE_TYPE_CHOICES = [
        ("T", "Tailor"),
        ("S", "Seller"),
    ]

    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Search(models.Model):
    term = models.CharField(max_length=300)
    time = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    GENDER_CHOICES = [
        ("U", "Unisex"),
        ("M", "Male"),
        ("F", "Female")
    ]

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
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, default="U")

    supplier = models.ForeignKey(
        Suplier, on_delete=models.DO_NOTHING, null=True)
    buying_price = models.FloatField()
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    added_at = models.DateTimeField(auto_now_add=True)

    suplier_paid = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name


class SavedProducts(models.Model):
    item = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    date_added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)


class Message(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
