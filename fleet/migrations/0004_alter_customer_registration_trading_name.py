# Generated by Django 5.1.4 on 2025-01-15 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fleet', '0003_rename_customer_name_customer_registration_trading_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_registration',
            name='trading_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
