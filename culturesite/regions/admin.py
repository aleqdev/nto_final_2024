from django.contrib import admin

from .models import Region, City


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    pass


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass
