from datetime import datetime

from django.db import models

# Create your models here.


class Customer(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    joined = models.DateTimeField(default=datetime.now())
    image = models.ImageField(upload_to='customers/customer_images', blank=True, null=True)

    def __str__(self):
        return self.email
