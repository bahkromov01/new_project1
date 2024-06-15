from django.db import models

# Create your models here.


# Product => title, description, price, rating, discount, quantity
# Image => image, product => fk


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    price = models.FloatField()
    rating = models.FloatField()
    discount = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)

    def get_attributes(self) -> list[dict]:
        product_attribute = ProductAttribute.objects.filter(product=self)
        attribute = []
        for pa in product_attribute:
            attribute.append({
                'attribute_key': pa.attiribute.key_name,
                'attribute_value': pa.attiribute_value.value_name
            })  # [{}, {}, {} ]
        return attribute


    @property
    def discounted_price(self):
        if self.discount > 0:
            return self.price * (1 - self.discount / 100)
        return self.price

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to='products', null=True)
    product = models.ForeignKey('app.Product', on_delete=models.SET_NULL, related_name='image', null=True)


class Attributes(models.Model):
    key_name = models.CharField(max_length=125, null=True)

    def str(self):
        return self.key_name


class AttiributeValue(models.Model):
    value_name = models.CharField(max_length=125, null=True)

    def str(self):
        return self.value_name


class ProductAttribute(models.Model):
    product = models.ForeignKey('app.Product', on_delete=models.CASCADE)
    attiribute = models.ForeignKey('app.Attributes', on_delete=models.CASCADE)
    attiribute_value = models.ForeignKey('app.AttiributeValue', on_delete=models.CASCADE)


class Customer(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    join_date = models.DateTimeField(auto_now_add=True)
    address = models.TextField()

    def __str__(self):
        return f"{self.full_name}"
