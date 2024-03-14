from django.contrib import admin
from .models import Place, EventType, Event
from import_export.admin import ImportExportModelAdmin


@admin.register(Place)
class PlaceAdmin(ImportExportModelAdmin):
    list_display = ["object", "id", "name", "capacity"]

    def object(self, obj):
        return str(obj)
    
    object.short_description = 'Объект'
    

@admin.register(EventType)
class EventTypeAdmin(ImportExportModelAdmin):
    list_display = ["type_name", "id"]
    

@admin.register(Event)
class EventAdmin(ImportExportModelAdmin):
    list_display = ["object", "id", "date", "name", "event_type", "datetime_begin", "datetime_end", "visitors_count", "place", "is_paid"]

    def object(self, obj):
        return str(obj)
    
    object.short_description = 'Объект'
    