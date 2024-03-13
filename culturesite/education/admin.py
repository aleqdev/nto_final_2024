from django.contrib import admin
from .models import Studies, TeacherEducation
from import_export.admin import ImportExportModelAdmin

@admin.register(Studies)
class StudiesAdmin(ImportExportModelAdmin):
    pass

@admin.register(TeacherEducation)
class TeacherEducationAdmin(ImportExportModelAdmin):
    pass

