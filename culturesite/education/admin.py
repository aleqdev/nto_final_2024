from django.contrib import admin
from .models import Study, TeacherEducation
from import_export.admin import ImportExportModelAdmin
from .resources import StudiesResource

@admin.register(Study)
class StudyAdmin(ImportExportModelAdmin):
    list_display = ["id", "name"]
    resource_class = StudiesResource


@admin.register(TeacherEducation)
class TeacherEducationAdmin(ImportExportModelAdmin):
    pass
