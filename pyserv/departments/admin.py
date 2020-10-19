from django.contrib import admin
from departments.models import DepartmentObjects, Department, DepartmentPerson, DepartmentObjectCase
from offers.models import DepObjectsInOffer

# class DepartmentObjectsInline(admin.TabularInline):
#     model = DepartmentObjects
#     extra = 1



class DepObjectsInOfferInline(admin.TabularInline):
    model = DepObjectsInOffer
    extra = 1


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    list_filter = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('id',)


@admin.register(DepartmentPerson)
class DepartmentPersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'department', 'description', 'birthday')
    list_filter = ('name', 'created_at', 'updated_at')
    search_fields = ('name', 'position', 'skill')
    prepopulated_fields = {'slug': ('name', 'birthday')}
    ordering = ('name',)


@admin.register(DepartmentObjectCase)
class DepartmentObjectCaseAdmin(admin.ModelAdmin):
    list_display = ('object_code', 'title', 'is_active')
    list_filter = ('object_code', 'title', 'is_active', 'created_at', 'updated_at')
    search_fields = ('object_code', 'title',)
    prepopulated_fields = {'slug': ('object_code', 'title')}
    ordering = ('object_code',)
