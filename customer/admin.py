from email.headerregistry import Address

from django.contrib import admin

from customer.models import Customer, User


# Register your models here.

# admin.site.register(Customer)


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email', 'is_active']
    search_fields = ['email', 'id']
    list_filter = ['joined', 'is_active']
    list_per_page = 2
