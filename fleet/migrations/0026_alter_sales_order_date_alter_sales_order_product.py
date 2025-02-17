# Generated by Django 5.1.4 on 2025-02-09 15:07

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fleet', '0025_alter_route_checkpoints_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales_order',
            name='date',
            field=models.DateField(default=datetime.datetime.today),
        ),
        migrations.AlterField(
            model_name='sales_order',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fleet.products'),
        ),
    ]
