# Generated by Django 5.1.4 on 2025-02-10 21:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fleet', '0030_alter_transporter_order_route'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transporter_order',
            name='route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fleet.route'),
        ),
    ]
