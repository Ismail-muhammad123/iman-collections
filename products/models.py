from email.policy import default
from django.db import models
from django.utils.text import slugify
from store.models import Store


class Size(models.Model):
    name = models.CharField(max_length=100, unique=True)
    added_at = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(
        "user.User",
        on_delete=models.DO_NOTHING,
        limit_choices_to={"staff": True},
        related_name="sizes_added",
    )

    def __str__(self) -> str:
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=100, unique=True)
    color_hex_code = models.CharField(max_length=20)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to="categories", blank=True)
    added_at = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(
        "user.User",
        on_delete=models.DO_NOTHING,
        limit_choices_to={"staff": True},
        related_name="categories_added",
    )
    slug = models.CharField(max_length=200, blank=True, default="")

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, related_name="sub_categories"
    )
    image = models.ImageField(upload_to="sub_categories/", blank=True)
    added_at = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(
        "user.User",
        on_delete=models.DO_NOTHING,
        limit_choices_to={"staff": True},
        related_name="sub_categories_added",
    )
    slug = models.CharField(max_length=200, blank=True, default="", unique=True)

    class Meta:
        verbose_name_plural = "sub categories"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(SubCategory, self).save(*args, **kwargs)


class Product(models.Model):
    GENDER_CHOICES = [("M", "Male"), ("F", "Female"), ("U", "Unisex")]

    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, related_name="products"
    )

    sub_category = models.ForeignKey(
        SubCategory, on_delete=models.SET_NULL, null=True, related_name="products"
    )
    delivery_days = models.PositiveIntegerField()
    description = models.TextField()
    on_sale = models.BooleanField(default=False)
    store = models.ForeignKey(
        Store, on_delete=models.SET_NULL, null=True, related_name="products"
    )
    # images = models.ManyToManyField("ProductImage", related_name="products")
    # variants = models.ManyToManyField("ProductVariant", related_name="products")

    is_active = models.BooleanField(default=True)

    added_at = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(
        "user.User",
        on_delete=models.DO_NOTHING,
        limit_choices_to={"staff": True},
        related_name="products_added",
    )

    slug = models.CharField(max_length=200, blank=True, default="")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


class ProductVariant(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_variants"
    )
    size = models.ForeignKey(
        Size, on_delete=models.SET_NULL, null=True, related_name="product_variants"
    )
    color = models.ForeignKey(
        Color, on_delete=models.SET_NULL, null=True, related_name="product_variants"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    track_inventory = models.BooleanField(default=True)
    available_quantity = models.PositiveIntegerField()
    image = models.ImageField(upload_to="product_images/")
    active = models.BooleanField(default=True)

    def as_dict(self):
        return {
            "product": self.product,
            "size": self.size,
            "color": self.color,
            "price": self.price,
            "available_quantity": self.available_quantity,
            "image": self.image,
        }

    def __str__(self):
        return f"{self.product.name} - {self.size.name} - {self.color.name}"


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_images"
    )
    image = models.ImageField(upload_to="product_images/")


class Cart(models.Model):
    product_variant = models.ForeignKey(
        ProductVariant, on_delete=models.SET_NULL, null=True
    )
    quantity = models.PositiveIntegerField()
    added_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        "user.User",
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        related_name="cart",
    )

    device = models.CharField(max_length=100, null=True, blank=True, default="")

    class Meta:
        verbose_name_plural = "Cart"

    def __str__(self) -> str:
        return f"{self.product_variant.product.name} x {self.quantity}"
