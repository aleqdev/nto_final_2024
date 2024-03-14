from django.contrib import admin
from .models import Artifact, ForeignOrganization, ShowcaseType, Showcase
from import_export.admin import ImportExportModelAdmin
from .resources import ArtifactResource, ForeignOrganizationResource, ShowcaseTypeResource, ShowcaseResource

@admin.register(Artifact)
class ArtifactAdmin(ImportExportModelAdmin):
    list_display = ["name", "owner", "id"]
    resource_class = ArtifactResource


@admin.register(ForeignOrganization)
class ForeignOrganizationAdmin(ImportExportModelAdmin):
    list_display = ["name", "id"]
    resource_class = ForeignOrganizationResource


@admin.register(ShowcaseType)
class ShowcaseTypeAdmin(ImportExportModelAdmin):
    list_display = ["name", "id"]
    resource_class = ShowcaseTypeResource


@admin.register(Showcase)
class ShowcaseAdmin(ImportExportModelAdmin):
    list_display = ["name", "type", "id"]
    resource_class = ShowcaseResource
