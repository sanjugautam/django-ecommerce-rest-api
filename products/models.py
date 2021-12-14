from django.db import models

# Create your models here.
from core.models import Customer


class Product(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=80, blank=False)
    seller = models.OneToOneField(Customer, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    warehouse_location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id}: {self.name}"
