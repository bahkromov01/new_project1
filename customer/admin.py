from email.headerregistry import Address

from django.contrib import admin
from django.contrib.auth.models import AbstractUser
from adminsortable2.admin import SortableAdminMixin
from customer.models import Customer, User, SortableBook


# Register your models here.

# admin.site.register(Customer)

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email']
    search_fields = ['email', 'id']
    list_filter = ['joined', 'full_name']
    list_per_page = 5

    def has_add_permission(self, request):
        return True

    def has_view_or_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(SortableBook)
class SortableBookAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass