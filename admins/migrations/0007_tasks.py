# Generated by Django 5.0.6 on 2024-07-10 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0006_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.TextField()),
            ],
        ),
    ]
