# Generated by Django 5.1.4 on 2025-01-15 12:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fleet', '0002_remove_sales_order_sales_order_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer_registration',
            old_name='customer_name',
            new_name='trading_name',
        ),
        migrations.RemoveField(
            model_name='customer_registration',
            name='email',
        ),
        migrations.RemoveField(
            model_name='fuel_service_providers',
            name='email',
        ),
        migrations.RemoveField(
            model_name='route',
            name='offloading_point',
        ),
        migrations.RemoveField(
            model_name='transporter_order',
            name='sale_order_number',
        ),
        migrations.AddField(
            model_name='customer_registration',
            name='email_address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='fuel_service_providers',
            name='email_address',
            field=models.EmailField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='route',
            name='offloading_points',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sales_order',
            name='UOM',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='transporter_order',
            name='POD_number',
            field=models.CharField(default=1, max_length=200),
        ),
        migrations.AddField(
            model_name='transporter_order',
            name='sales_order_number',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='transporter_registration',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='transporter_statement',
            name='date_from',
            field=models.DateField(default=datetime.datetime.today),
        ),
        migrations.AlterField(
            model_name='transporter_statement',
            name='date_to',
            field=models.DateField(default=datetime.datetime.today),
        ),
    ]
