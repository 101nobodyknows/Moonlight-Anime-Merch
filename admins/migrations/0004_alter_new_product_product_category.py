# Generated by Django 5.0.6 on 2024-07-04 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0003_remove_new_product_product_review_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_product',
            name='product_category',
            field=models.CharField(choices=[('Clothing', 'Clothing'), ('Footwear', 'Footwear'), ('Accessories', 'Accessories'), ('Jewellery', 'Jewellery')], max_length=20),
        ),
    ]