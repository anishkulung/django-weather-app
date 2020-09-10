from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length = 200,help_text = "Enter product name")
    def __str__(self):
        return self.product_name

class ProductDetail(models.Model):
    year = models.IntegerField()
    product = models.ForeignKey('Product',on_delete=models.CASCADE)
    sales = models.FloatField()
    def __str__(self):
        return f"{self.product} - {self.year}"