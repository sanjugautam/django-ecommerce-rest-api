from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Customer(AbstractUser):
    full_name = models.CharField(max_length=100)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'Customers'
