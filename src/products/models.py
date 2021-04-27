from django.db import models

# Create your models here.

class Products(models.Model):
    title = models.CharField(max_length = 120)
    description =models.TextField(blank = True, null = True)
    price = models.DecimalField(max_digits=1000, decimal_places=2)
    summary = models.TextField(default = "OK!")
    featured = models.BooleanField()
    bio = models.BooleanField()