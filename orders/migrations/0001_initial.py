# Generated by Django 3.2.9 on 2021-12-14 08:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=120)),
                ('status', models.CharField(choices=[('Not Shipped Yet', 'Not Shipped Yet'), ('Shipped', 'Shipped'), ('Cancelled', 'Cancelled'), ('Refunded', 'Refunded'), ('Delivered', 'Delivered')], default='Not Shipped Yet', max_length=120)),
                ('order_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=100)),
                ('shipping_address', models.CharField(max_length=200)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Orders',
            },
        ),
    ]
