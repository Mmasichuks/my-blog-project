from django.db import models
from account.models import User
from django.utils.translation import  gettext_lazy as _
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    name = models.CharField( max_length=150)
    slug = models.SlugField()
    created = models.DateTimeField( auto_now=False, auto_now_add=False)

    class Meta:
          verbose_name = 'Category'
          verbose_name_plural ='Categories'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            super().save(*args, **kwargs)

    def __str__(self):
        return f' categories for {self.name}'
 
       


    
class Product(models.Model):
    name = models.CharField( max_length=150)
    slug = models.SlugField()
    category = models.ForeignKey("product.Category",null =True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User,verbose_name=_("User"), on_delete=models.CASCADE)
    date = models.DateField()
    description = models.TextField()
    price = models.FloatField()
    image =models.ImageField( upload_to='media',null=True ,blank=True)

    def __str__(self):
        return f'{self.category} || {self.name}'

    






