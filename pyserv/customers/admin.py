from django.contrib import admin
from customers.models import Customer, CustomerPerson, CustomerRequest


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'division', 'description', 'location')
    list_filter = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)
   # prepopulated_fields = {'slug': ('name', 'division')}
    ordering = ('name',)


@admin.register(CustomerPerson)
class CustomerPersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'customer', 'description',)
    list_filter = ('name', 'created_at', 'updated_at')
    search_fields = ('name', 'position', 'customer')
    prepopulated_fields = {'slug': ('name', 'customer')}
    ordering = ('customer', 'name')


@admin.register(CustomerRequest)
class CustomerRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'customer', 'person', 'created_at', 'folder')
    list_filter = ('title', 'customer', 'person', 'created_at')
    search_fields = ('title', 'customer')
    prepopulated_fields = {'slug': ('title', 'created_at')}
    ordering = ('customer',)

