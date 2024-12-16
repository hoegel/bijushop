from django.db import models
from django.urls import reverse

class Product(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, default='', unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=500)
    availability = models.BooleanField(default=True)
    composition = models.TextField(max_length=500)
    image = models.ImageField(upload_to='products/', blank = True, null = True)
    #category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.slug)])
