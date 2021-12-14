from django.contrib import admin
from .models import Product


class AreaInline(admin.StackedInline):
    model = Product


# Register your models here.
admin.site.register(Product)
