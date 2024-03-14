from django.contrib import admin
from .models import Place, Location, EventType, Event, UnitPlace, UnitPlacePurchase
from import_export.admin import ImportExportModelAdmin


from rangefilter.filters import (
    DateRangeFilterBuilder,
    DateTimeRangeFilterBuilder,
    NumericRangeFilterBuilder,
    DateRangeQuickSelectListFilterBuilder,
)

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


class IsFree(admin.SimpleListFilter):
    title = 'Фильтр мест по занятости'
    parameter_name = 'price'

    def lookups(self, request, model_admin):
        return (
            ('True', 'Свободные'), 
            ('False', 'Занятые')
        )

    def queryset(self, request, queryset):
        value = self.value()

        if value is None:
            return queryset

        exc = []
        for q in queryset:
            purchase = UnitPlacePurchase.objects.filter(
                row=q.row,
                column=q.column,
                location=q.location,
                event=q.event
            )
            if value == 'True' and len(purchase) == 0:
                exc.append(q.id)
            if value == 'False' and len(purchase) != 0:
                exc.append(q.id)

        return queryset.filter(id__in=exc)
    

class FilterLocation(admin.SimpleListFilter):
    title = 'Фильтр мест по пространству'
    parameter_name = 'id'

    def lookups(self, request, model_admin):
        return tuple(
            (place.id, place.name)
            for place
            in Place.objects.all()
        )

    def queryset(self, request, queryset):
        value = self.value()

        if value is None:
            return queryset
        
        print(value)

        return queryset.filter(location__place__id__exact=int(value))
    

@admin.register(UnitPlace)
class UnitPlaceAdmin(ImportExportModelAdmin):
    list_display = ["object", "price", "is_free"]
    list_filter = [IsFree, FilterLocation]
    action_form = ChangePriceForm
    actions = ["change_price", "sell_ticket"]
    search_fields = ["row", "column", "object", "price"]

    def object(self, obj):
        return str(obj)
    object.short_description = 'Объект'

    def is_free(self, obj):
        return "Свободное" if obj.is_free() else "Занятое"
    is_free.short_description = "Занятость"

    def change_price(modeladmin, request, queryset):
        queryset.update(price=int(request.POST['price'] or '0'))
    change_price.short_description = "Изменить цену"

    def sell_ticket(modeladmin, request, queryset):
        import datetime
        from django.core.exceptions import ValidationError

        for item in queryset:
            if not item.is_free():
                continue
            
            UnitPlacePurchase.objects.create(
                datetime=datetime.datetime.now(),
                event=item.event,
                location=item.location,
                row=item.row,
                column=item.column,
                price=item.price
            )

    sell_ticket.short_description = "Продать билеты"
    
from datetime import datetime
@admin.register(UnitPlacePurchase)
class UnitPlacePurchaseAdmin(ImportExportModelAdmin):
    list_display = ["object", "id", "datetime", "event", "location", "row", "column", "price"]
    list_filter = ["price", "location", "event", ("datetime", DateRangeFilterBuilder()),
        (
            "datetime",
            DateTimeRangeFilterBuilder(
                title="Custom title",
                default_start=datetime(2020, 1, 1),
                default_end=datetime(2030, 1, 1),
            ),
        ),]
    search_fields = ["price", "location__name", "row", "column", "event"]
    def object(self, obj):
        return str(obj)
    
    object.short_description = 'Объект'
    