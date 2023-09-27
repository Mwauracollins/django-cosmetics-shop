from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from PIL import Image


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)  # Call the real save() method

    class Meta:
        db_table = 'Category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products', null=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)

        super(Product, self).save(*args, **kwargs)  # Call the real save() method

        img = Image.open(self.image.path)

        desired_width = 200
        desired_height = 300

        img.thumbnail((desired_width, desired_height))

        img.save(self.image.path)

    def get_absolute_url(self):
        return reverse("shop:product_detail", kwargs={"slug": self.slug})

    class Meta:
        db_table = 'Product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Wishlist(models.Model):
    from accounts.models import Profile

    user = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user

    class Meta:
        db_table = 'Wishlist'
        verbose_name = 'Wishlist'
        verbose_name_plural = 'Wishlists'
