# Generated by Django 5.1.4 on 2025-02-03 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fleet', '0011_sales_order_number_of_trucks_remaining'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales_order',
            name='number_of_trucks_alocated',
            field=models.IntegerField(default=0),
        ),
    ]
