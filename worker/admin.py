from django.contrib import admin
from .models import Worker, Visit, Unit


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number')
    search_fields = ('name',)


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'worker')
    search_fields = ('name',)


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ('unit', 'datetime', 'latitude', 'longitude')
    search_fields = ('unit__name', 'unit__worker__name')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
