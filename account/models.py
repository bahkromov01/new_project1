from django.db import models

# Create your models here.


class Login(models.Model):
    email = models.EmailField(max_length=50, blank=True, null=True)
    password = models.IntegerField()

    def __str__(self):
        return self.email
