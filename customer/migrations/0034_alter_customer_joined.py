# Generated by Django 5.0.6 on 2024-06-23 16:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0033_alter_customer_joined_user_delete_customeruser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='joined',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 23, 21, 43, 57, 494097)),
        ),
    ]
