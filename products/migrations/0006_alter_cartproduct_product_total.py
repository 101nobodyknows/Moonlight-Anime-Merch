# Generated by Django 5.0.6 on 2024-07-14 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_cartproduct_product_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartproduct',
            name='product_total',
            field=models.IntegerField(default=0),
        ),
    ]