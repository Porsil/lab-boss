from django.contrib import admin
from .models import Material, Batch


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):

    list_display = ('name', 'status',)
    list_filter = ('name', 'status')
    search_fields = ['name', 'status']


@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):

    list_display = ('priority', 'batch', 'status',)
    list_filter = ('priority', 'batch', 'status',)
    search_fields = ['batch']
    actions = ['approve_batch']

    def approve_batch(self, request, queryset):
        queryset.update(status="Approved")
