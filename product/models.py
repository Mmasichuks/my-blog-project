from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class category(models.Model):
     name = models.CharField( max_length=150)
     slug = models.SlugField()
     created = models.DateTimeField( auto_now=False, auto_now_add=False)
    
class Product(models.Model):
    name = models.CharField( max_length=150)
    slug = models.SlugField()
    category = models.ForeignKey("product.category", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.TextField()
    price = models.FloatField()

    






