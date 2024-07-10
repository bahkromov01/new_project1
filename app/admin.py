from django.contrib import admin
from app.models import Product, Image, ProductAttribute, Attributes, AttiributeValue
# Register your models here.


# admin.site.register(Product, ProductAdmin)
admin.site.register(Image)
admin.site.register(ProductAttribute)
admin.site.register(Attributes)
admin.site.register(AttiributeValue)


class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'discount', 'price')
    list_filter = ('name',)
    list_per_page = 2



admin.site.register(Product, ProductModelAdmin)


