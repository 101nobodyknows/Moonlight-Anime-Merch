# Generated by Django 5.0.6 on 2024-08-26 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0009_new_product_actual_prod_price_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='new_product',
            old_name='discount_price',
            new_name='discount_value',
        ),
    ]
