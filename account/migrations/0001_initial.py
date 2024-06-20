# Generated by Django 5.0.6 on 2024-06-20 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('password', models.IntegerField(max_length=8)),
            ],
        ),
    ]
