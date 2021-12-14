from django.db import models

# Create your models here.
from django.db.models.signals import pre_save

from core.models import Customer
from orders.order_utils import unique_order_id_generator

ORDER_STATUS_CHOICES = (
    ('Not Shipped Yet', 'Not Shipped Yet'),
    ('Shipped', 'Shipped'),
    ('Cancelled', 'Cancelled'),
    ('Refunded', 'Refunded'),
    ('Delivered', 'Delivered')
)


class Orders(models.Model):
    order_id = models.CharField(max_length=120, blank=True, primary_key=True)
    buyer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.CharField(max_length=120, default='Not Shipped Yet', choices=ORDER_STATUS_CHOICES)
    order_price = models.DecimalField(default=0.0, max_digits=100, decimal_places=2, blank=False)
    shipping_address = models.CharField(max_length=200, blank=False)

    class Meta:
        db_table = 'Orders'

    def __str__(self):
        return self.order_id


def pre_save_create_order_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = unique_order_id_generator(instance)


pre_save.connect(pre_save_create_order_id, sender=Orders)
