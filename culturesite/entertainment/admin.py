from django.contrib import admin
from .models import Place, Location, EventType, Event, UnitPlace, UnitPlacePurchase
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
    price = forms.IntegerField(required=False, validators=[MinValueValidator(0)], label="Цена")


class IsFree(admin.FieldListFilter):
    title = 'is free'
    parameter_name = 'is_free'

    def lookups(self, request, model_admin):
        return (
            ('True', 'Yes'), 
            ('False', 'No')
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value == 'True':
            return queryset.exclude(external_number__exact='')
        elif value == 'False':
            return queryset.filter(external_number__exact='')
        return queryset
    

@admin.register(UnitPlace)
class UnitPlaceAdmin(ImportExportModelAdmin):
    list_display = ["object", "price", "is_free"]
    # list_filter = [("is_free", IsFree)]
    action_form = ChangePriceForm
    actions = ["change_price", "sell_ticket"]
    search_fields = ["row", "column", "object", "price"]

    def object(self, obj):
        return str(obj)
    object.short_description = 'Объект'

    def change_price(modeladmin, request, queryset):
        queryset.update(price=int(request.POST['price'] or '0'))
    change_price.short_description = "Изменить цену"

    def sell_ticket(modeladmin, request, queryset):
        import datetime
        for item in queryset:
            UnitPlacePurchase.objects.create(
                datetime=datetime.datetime.now(),
                event=item.event,
                location=item.location,
                row=item.row,
                column=item.column,
                price=item.price
            )

    sell_ticket.short_description = "Продать билеты"
    

@admin.register(UnitPlacePurchase)
class UnitPlacePurchaseAdmin(ImportExportModelAdmin):
    list_display = ["object", "id", "datetime", "event", "location", "row", "column", "price"]
    list_filter = ["price", "location", "event"]
    search_fields = ["price", "location__name", "row", "column", "event"]
    def object(self, obj):
        return str(obj)
    
    object.short_description = 'Объект'
    