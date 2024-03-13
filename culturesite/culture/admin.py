from django.contrib import admin
from .models import Artifact
from import_export.admin import ImportExportModelAdmin
from .resources import ArtifactResource

@admin.register(Artifact)
class ArtifactAdmin(ImportExportModelAdmin):
    list_display = ["id", "name", "owner"]
    resource_class = ArtifactResource
