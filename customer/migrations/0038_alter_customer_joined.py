# Generated by Django 5.0.6 on 2024-06-23 17:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0037_alter_customer_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='joined',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 23, 22, 9, 34, 73643)),
        ),
    ]
