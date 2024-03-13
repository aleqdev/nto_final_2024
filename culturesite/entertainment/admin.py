from django.contrib import admin
from .models import Place
from import_export.admin import ImportExportModelAdmin


@admin.register(Place)
class PlaceAdmin(ImportExportModelAdmin):
    list_display = ["id", "name", "capacity"]
    