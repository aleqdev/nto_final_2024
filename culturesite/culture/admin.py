from django.contrib import admin

from .models import Artifact


@admin.register(Artifact)
class PlaceAdmin(admin.ModelAdmin):
    pass
