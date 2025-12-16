from django.db import models
from django.utils.text import slugify
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()# null = True
    price = models.DecimalField(max_digits=8, decimal_places=2)
    color = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    brand = models.CharField(max_length=20)
    dev_country = models.CharField(max_length=20)
    image = models.ImageField(upload_to="products/", null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
def __str__(self):
    return f"{self.brand} {self.name}"

class Category(models.Model):
    """Категорія товарів (смартфони, планшети, аксесуари)"""
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

class Order(models.Model):
    """Замовлення товару"""
    id = models.AutoField(primary_key=True)
    #order_number =
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    #status = models.CharField(max_length=20, choices=
    #    ('pending', 'Pendeng')
    #    ()



