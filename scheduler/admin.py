from django.contrib import admin
from .models import Analyst, Test, Workload


@admin.register(Analyst)
class AnalystAdmin(admin.ModelAdmin):

    list_display = ('work_id', 'name', 'status',)
    list_filter = ('work_id', 'name', 'status',)
    search_fields = ['work_id', 'name', 'status']


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):

    list_display = ('name', 'status',)
    list_filter = ('name', 'status',)
    search_fields = ['name', 'status']


@admin.register(Workload)
class WorkloadAdmin(admin.ModelAdmin):

    list_display = ('test_date', 'analyst', 'test', 'status',)
    list_filter = ('test_date', 'status',)
    search_fields = ['test_date', 'status']
