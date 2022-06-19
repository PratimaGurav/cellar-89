from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=250)
    friendly_name = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True,
        on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    country = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2,
        null=True, blank=True
    )
    alcohol_percentage = models.DecimalField(
        max_digits=3, decimal_places=1,
        null=True, blank=True
    )
    grape_variety = models.CharField(max_length=254)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):

    RATING_CHOICES = [ 
        (5, '5'),
        (4, '4'),
        (3, '3'),
        (2, '2'),
        (1, '1'),
    ]
    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    product_rating = models.IntegerField(
        choices=RATING_CHOICES,
        default=5
    )
    title = models.CharField(
        verbose_name=('Review Title'),
        max_length=25,
        null=False,
        blank=False
    )
    user_review = models.TextField(
        verbose_name=('User Review'),
        max_length=250,
        null=False,
        blank=False
    )
    created_on = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f'{self.title}'