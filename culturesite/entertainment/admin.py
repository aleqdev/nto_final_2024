from django.contrib import admin
# from person.models import Person

from .models import Place


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    pass
