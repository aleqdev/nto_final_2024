from django.contrib import admin
from .models import Artifact, ForeignOrganization, ShowcaseType, Showcase, ArtifactReturnAct, ShowcaseOrder, ArtifactTransportAct, ArtifactAquireAct
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


class ShowcaseOrderForm(forms.ModelForm):
    class Meta:
        model = Showcase
        exclude = tuple()

    def clean(self):
        from django.forms import ValidationError

        showcase = self.cleaned_data['showcase'] 
        artifacts = self.cleaned_data['artifacts'] 
        
        for artifact in artifacts:
            print(showcase.type.name)
            if showcase.type.name == "Внутренняя" and artifact.owner_study is None:
                raise ValidationError({
                    "artifacts": "Выбран экспонат, принадлежащий сторонней организации!"
                })
            
            if showcase.type.name == "Внешняя" and artifact.owner_foreign_organization is None:
                raise ValidationError({
                    "artifacts": "Выбран экспонат, не принадлежащий сторонней организации!"
                })
    

@admin.register(Showcase)
class ShowcaseAdmin(ImportExportModelAdmin):
    list_display = ["name", "type", "id"]
    resource_class = ShowcaseResource



@admin.register(ArtifactReturnAct)
class ArtifactReturnActAdmin(ImportExportModelAdmin):
    list_display = ["showcase_order", "datetime", "id"]
    resource_class = ArtifactReturnActResource

admin.site.register(ArtifactAquireAct)
admin.site.register(ArtifactTransportAct)

@admin.register(ShowcaseOrder)
class ShowcaseOrderAdmin(ImportExportModelAdmin):
    form = ShowcaseOrderForm
    list_display = ["showcase", "study", "place", "date_start", "date_end", "date_register"]
    def study(self, obj):
        status = "В ожидании поступления экспонатов от сторонней организации"
        find = ArtifactTransportAct.objects.filter(showcase_order=obj)
        if (find.count() > 0):
            status = "Переданы на выставку."
        find = ArtifactReturnAct.objects.filter(showcase_order=obj)
        if (find.count() > 0):
            status = "Экспонаты возвращены."
        return status
    study.short_description = 'Стадия'