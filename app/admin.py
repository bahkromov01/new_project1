from django.contrib import admin
from app.models import Product, Image,ProductAttribute, Attributes, AttiributeValue
# Register your models here.


admin.site.register(Product)
admin.site.register(Image)
admin.site.register(ProductAttribute)
admin.site.register(Attributes)
admin.site.register(AttiributeValue)