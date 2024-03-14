from django.contrib import admin
<<<<<<< HEAD
from .models import Artifact, ForeignOrganization, ShowcaseType, Showcase, ArtifactReturnAct
=======
from .models import Artifact, ForeignOrganization, ShowcaseType, Showcase, OrderExhibition
>>>>>>> 14707fa0dd750d2b7f713e770816c4f5849e6ff0
from import_export.admin import ImportExportModelAdmin
from .resources import ArtifactResource, ForeignOrganizationResource, ShowcaseTypeResource, ShowcaseResource, ArtifactReturnActResource
from django import forms


class ArtifactForm(forms.ModelForm):
    def clean(self):
        owner_study = self.cleaned_data['owner_study']
        owner_foreign_organization = self.cleaned_data['owner_foreign_organization']
        if owner_study is None and owner_foreign_organization is None:
            raise forms.ValidationError({
                'owner_study': "Владелец не выбран"
            })
        
        if owner_study is not None and owner_foreign_organization is not None:
            raise forms.ValidationError({
                'owner_foreign_organization': "Выберите одного владельца"
            })


@admin.register(Artifact)
class ArtifactAdmin(ImportExportModelAdmin):
    form = ArtifactForm
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


@admin.register(ArtifactReturnAct)
class ArtifactReturnActAdmin(ImportExportModelAdmin):
    list_display = ["showcase_order", "datetime", "id"]
    resource_class = ArtifactReturnActResource
    
admin.site.register(OrderExhibition)
