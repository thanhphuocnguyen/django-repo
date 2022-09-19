from time import timezone
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from versatileimagefield.fields import VersatileImageField, PPOIField


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField(max_length=255)

    def __str__(self) -> str:
        return self.name


class ProductSize(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Cateogry(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ManyToManyField(Cateogry, related_name='products')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    image = models.ManyToManyField('product_reviewer.Image',
                                   related_name='products')

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name


class ProductSite(models.Model):
    name = models.CharField(max_length=255)
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='sites',
                                related_query_name='site')
    company = models.ForeignKey(Company,
                                on_delete=models.CASCADE,
                                related_name='sites',
                                related_query_name='site')
    productsize = models.ForeignKey(ProductSize,
                                    on_delete=models.CASCADE,
                                    related_name='sites',
                                    related_query_name='site')
    price = models.DecimalField(max_digits=9, decimal_places=2)
    url = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='comments',
                                related_query_name='comment')
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='comments',
                             related_query_name='commnet')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class CustomerReportRecord(models.Model):
    time_raised = models.DateTimeField(
        default=timezone.now,
        editable=False,
    )
    reference = models.CharField(unique=True, max_length=20)
    description = models.TextField()


class Image(models.Model):
    name = models.CharField(max_length=255)
    image = VersatileImageField('Image',
                                upload_to='images/',
                                ppoi_field='image_ppoi')
    image_ppoi = PPOIField()

    def __str__(self):
        return self.name
