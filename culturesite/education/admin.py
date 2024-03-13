from django.contrib import admin
from .models import Study, TeacherEducation
from import_export.admin import ImportExportModelAdmin


@admin.register(Study)
class StudyAdmin(ImportExportModelAdmin):
    list_display = ["id", "name"]


@admin.register(TeacherEducation)
class TeacherEducationAdmin(ImportExportModelAdmin):
    pass

