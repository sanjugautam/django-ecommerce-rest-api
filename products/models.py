from django.db import models

# Create your models here.
from core.models import Customer


class ProductCategory(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=80, blank=False)

    class Meta:
        db_table = "ProductCategory"
        verbose_name_plural = "ProductCategory"

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=80, blank=False)
    seller = models.ForeignKey(Customer, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    warehouse_location = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0, blank=False)
    price = models.DecimalField(decimal_places=2, blank=True, max_digits=7, default=0.0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, default=None)

    class Meta:
        db_table = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return f"{self.id}: {self.name}"

