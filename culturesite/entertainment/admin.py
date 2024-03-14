from django.contrib import admin
from .models import Place, Location, EventType, Event, UnitPlace
from import_export.admin import ImportExportModelAdmin



class LocationInline(admin.StackedInline):
    model = Location
    extra = 0
    verbose_name = "Локация"
    verbose_name_plural = "Локации"

@admin.register(Place)
class PlaceAdmin(ImportExportModelAdmin):
    list_display = ["object", "id", "name", "capacity"]
    inlines = [LocationInline]

    def object(self, obj):
        return str(obj)
    
    object.short_description = 'Объект'

# class BookInline(admin.StackedInline):
#     model = Book
#     extra = 0
#     verbose_name = "Книга автора"
#     verbose_name_plural = "Книги автора"
#     # readonly_fields = ("price", ) # readonly поля
#     # fields = ("name", "price", ) # можно указать какие поля выводить
#     min_num = 0 # минимальное количество пустых полей для заполнения
#     max_num = 100 # максимальное количество пустых полей для заполнения
#     can_delete = True
#     show_change_link = True

# class AuthorAdmin(admin.ModelAdmin):
#     inlines = [
#         BookInline,
#     ]
    
# admin.site.register(Author, AuthorAdmin)
# admin.site.register(Book)
    

@admin.register(EventType)
class EventTypeAdmin(ImportExportModelAdmin):
    list_display = ["type_name", "id"]
    

@admin.register(Event)
class EventAdmin(ImportExportModelAdmin):
    list_display = ["object", "id", "date", "name", "event_type", "datetime_begin", "datetime_end", "visitors_count", "place", "is_paid"]

    def object(self, obj):
        return str(obj)
    
    object.short_description = 'Объект'
    

from django.contrib.admin.helpers import ActionForm
from django import forms
from django.core.validators import MinValueValidator


class ChangePriceForm(ActionForm):
    price = forms.IntegerField(required=True, validators=[MinValueValidator(0)], label="Цена")


@admin.register(UnitPlace)
class UnitPlaceAdmin(ImportExportModelAdmin):
    list_display = ["object", "price"]
    action_form = ChangePriceForm
    actions = ["change_price"]
    list_filter = ["event", ]
    search_fields = ["event", ]

    def object(self, obj):
        return str(obj)
    
    object.short_description = 'Объект'

    def change_price(modeladmin, request, queryset):
        queryset.update(price=int(request.POST['price']))

    change_price.short_description = "Изменить цену"
    