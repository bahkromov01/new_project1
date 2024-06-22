from datetime import datetime

from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

from customer.managers import CustomerUserManagers


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


class CustomerUser(AbstractUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)

    objects = CustomerUserManagers()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def str(self):
        return self.email

