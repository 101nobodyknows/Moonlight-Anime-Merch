# Generated by Django 5.0.6 on 2024-08-30 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0011_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='sub_content_sec',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='blog',
            name='sub_topic_sec',
            field=models.TextField(default=''),
        ),
    ]