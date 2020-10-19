from django.contrib import admin

from departments.admin import DepObjectsInOfferInline
from .models import CommercialOffer, ObjectCase, ObjectsInOffer, DepartmentOffer, DepartmentInCommercial


class ObjectsInOfferInline(admin.TabularInline):
    model = ObjectsInOffer
    extra = 1


class DepartmentInCommercialInline(admin.TabularInline):
    model = DepartmentInCommercial
    extra = 1


@admin.register(CommercialOffer)
class CommercialOfferAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'code', 'type', 'project_hh', 'commissioning_hh',
        'project_cost', 'commissioning_cost', 'material_cost',
        'total_cost'
    )
    list_filter = ('code', 'type', 'title', 'created_at', 'updated_at')
    search_fields = ('title', 'code')
    prepopulated_fields = {'slug': ('code', 'title')}
    ordering = ('code',)


@admin.register(ObjectCase)
class ObjectCaseAdmin(admin.ModelAdmin):
    list_display = ('title','object_code', 'description', 'created_at', 'is_active')
    list_filter = ('title','is_active', 'created_at', 'updated_at')
    search_fields = ('title', )
    ordering = ('id',)


@admin.register(DepartmentOffer)
class DepartmentOfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'code', 'type', 'project_hh', 'commissioning_hh')
    list_filter = ('code', 'type', 'title', 'created_at', 'updated_at')
    search_fields = ('title', 'code')
    prepopulated_fields = {'slug': ('code', 'title')}
    ordering = ('code',)
    inlines = (ObjectsInOfferInline, DepObjectsInOfferInline)



