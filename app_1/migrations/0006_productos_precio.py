# Generated by Django 3.2.12 on 2024-12-05 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0005_auto_20241204_2056'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='precio',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
