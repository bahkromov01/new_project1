# Generated by Django 5.0.6 on 2024-06-22 18:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_alter_customer_joined_alter_customeruser_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='joined',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 22, 23, 46, 52, 563968)),
        ),
    ]
