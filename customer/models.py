from datetime import datetime

from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

# from customer.managers import CustomerUserManagers
from customer.managers import CustomerUserManagers


# Create your models here.


class Customer(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    joined = models.DateTimeField(default=datetime.now())
    image = models.ImageField(upload_to='customers/customer_images', blank=True, null=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.email


class User(AbstractUser, PermissionsMixin,):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255, null=True)
    phone_number = models.CharField(max_length=13, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomerUserManagers()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class SortableBook(models.Model):
    title = models.CharField(
        "Title",
        max_length=255,
    )

    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    class Meta:
        ordering = ['my_order']
