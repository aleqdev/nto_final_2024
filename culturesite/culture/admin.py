from django.contrib import admin
from .models import Artifact, ArtifactOwner
from import_export.admin import ImportExportModelAdmin


@admin.register(Artifact)
class ArtifactAdmin(ImportExportModelAdmin):
    list_display = ["id", "name", "owner"]


@admin.register(ArtifactOwner)
class ArtifactOwnerAdmin(admin.ModelAdmin):
    pass
