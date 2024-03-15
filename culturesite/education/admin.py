from django.contrib import admin
from .models import Study, TeacherEducation, ActInviteStudy, Student, StudyStartOrder
from import_export.admin import ImportExportModelAdmin
from .resources import StudiesResource

class ActInviteStudyInline(admin.StackedInline):
    model = ActInviteStudy
    extra = 0
    verbose_name = "Заявка на посещение студии"
    verbose_name_plural = "Заявки на посещение студий"

class StudyStartOrderInline(admin.StackedInline):
    model = StudyStartOrder
    extra = 0
    verbose_name = "Приказ о работе студии"
    verbose_name_plural = "Приказы о работе студии"

@admin.register(StudyStartOrder)
class StudyStartOrderAdmin(ImportExportModelAdmin):
    # list_display = ["object", "id", "name", "capacity"]
    inlines = [ActInviteStudyInline]

    def object(self, obj):
        return str(obj)
    
    object.short_description = 'Объект'

@admin.register(Study)
class StudyAdmin(ImportExportModelAdmin):
    list_display = ["id", "name"]
    inlines = [StudyStartOrderInline]
    resource_class = StudiesResource


@admin.register(TeacherEducation)
class TeacherEducationAdmin(ImportExportModelAdmin):
    pass
