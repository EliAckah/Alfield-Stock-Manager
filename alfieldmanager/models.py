from django.db import models
from django.utils import timezone
from django.urls import reverse

class Product(models.Model):
    """A product that a worker can add"""
    name = models.CharField(max_length=200)
    sold = models.CharField(max_length=200)
    date_added = models.DateTimeField(default=timezone.now)
    in_stock = models.IntegerField(null=False)
    date_ordered = models.CharField(max_length=200)
    date_purchased = models.CharField(max_length=200)

    def __str__(self):
        """Return a string representation of the model"""
        return self.name
    def get_absolute_url(self):
        return reverse('product')