# Generated by Django 5.1.4 on 2025-01-07 14:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registered_name', models.CharField(max_length=200)),
                ('customer_name', models.CharField(max_length=200)),
                ('billing_address', models.CharField(max_length=200)),
                ('customer_TIN', models.CharField(max_length=200)),
                ('customer_VAT', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Fuel_Service_Providers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registered_name', models.CharField(max_length=200)),
                ('trading_name', models.CharField(max_length=200)),
                ('billing_address', models.CharField(max_length=200)),
                ('supplier_TIN', models.CharField(max_length=200)),
                ('supplier_VAT', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('product_description', models.CharField(max_length=200)),
                ('UOM', models.CharField(max_length=200)),
                ('truck_type', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_name', models.CharField(max_length=200)),
                ('loading_point', models.CharField(max_length=200)),
                ('offloading_point', models.CharField(max_length=200)),
                ('number_of_checkpoints', models.CharField(max_length=200)),
                ('checkpoints', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Sales_Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sales_order_number', models.CharField(max_length=200)),
                ('date', models.DateField(default=datetime.datetime.today)),
                ('customer', models.CharField(max_length=200)),
                ('product', models.CharField(max_length=200)),
                ('quantity', models.IntegerField(default=0)),
                ('truck_type', models.CharField(max_length=200)),
                ('number_of_trucks', models.IntegerField(default=0)),
                ('route', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Transporter_Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=200)),
                ('date', models.DateField(default=datetime.datetime.today)),
                ('sale_order_number', models.CharField(max_length=200)),
                ('transporter_name', models.CharField(max_length=200)),
                ('driver', models.CharField(max_length=200)),
                ('truck_reg_number', models.CharField(max_length=200)),
                ('trailer1_reg_number', models.CharField(max_length=200)),
                ('trailer2_reg_number', models.CharField(max_length=200)),
                ('container_number', models.CharField(max_length=200)),
                ('booking_ref', models.CharField(max_length=200)),
                ('route', models.CharField(max_length=200)),
                ('product', models.CharField(max_length=200)),
                ('charge', models.CharField(max_length=200)),
                ('charge_type', models.CharField(max_length=200)),
                ('linked_order', models.CharField(max_length=200)),
                ('customer_invoice_number', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Transporter_Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.today)),
                ('transporter', models.CharField(max_length=200)),
                ('payment_type', models.CharField(max_length=200)),
                ('source_ref', models.CharField(max_length=200)),
                ('truck_reg_number', models.CharField(max_length=200)),
                ('service_provider', models.CharField(max_length=200)),
                ('quantity', models.CharField(max_length=200)),
                ('unit_price', models.CharField(max_length=200)),
                ('payment_amount', models.CharField(max_length=200)),
                ('matched_orders', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Transporter_Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transporter_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Transporter_Statement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transporter_name', models.CharField(max_length=200)),
                ('date_from', models.DateField(default=datetime.date.today)),
                ('date_to', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Truck_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('truck_type', models.CharField(max_length=200)),
                ('load_tonnage', models.CharField(max_length=200)),
            ],
        ),
    ]
