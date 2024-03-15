from django.contrib import admin
from .models import Study, TeacherEducation, StudyStartOrder, Student, ActInviteStudy, TeacherReport
from import_export.admin import ImportExportModelAdmin
from .resources import StudiesResource
from django import forms


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


@admin.register(Study)
class StudyAdmin(ImportExportModelAdmin):
    list_display = ["id", "name"]
    inlines = [StudyStartOrderInline]
    resource_class = StudiesResource


@admin.register(TeacherEducation)
class TeacherEducationAdmin(ImportExportModelAdmin):
    pass


@admin.register(TeacherReport)
class TeacherReportAdmin(admin.ModelAdmin):
    change_list_template = 'admin/change_form_teacher_report.html'

    def get_queryset(self, request):
        return self.model.objects.all()
    
    def has_add_permission(self, request):
        return False
    

class StudyStartOrderForm(forms.ModelForm):
    class Meta:
        model = StudyStartOrder
        exclude = tuple()

    def clean(self):
        from django.forms import ValidationError

        date_begin = self.cleaned_data['date_begin'] 
        date_end = self.cleaned_data['date_end'] 
        teacher = self.cleaned_data['teacher'] 
        weekdays = self.cleaned_data['weekdays'] 
        time_begin = self.cleaned_data['time_begin'] 
        time_end = self.cleaned_data['time_end']

        if date_begin > date_end:
            raise ValidationError({
                "date_end": "Дата окончания работы студии раньше даты начала работы!"
            })
        
        if time_begin > time_end:
            raise ValidationError({
                "time_end": "Время окончания заятий раньше времени начала занятий!"
            })
        
        if not teacher.is_free(date_begin,
                               date_end,
                               [w.id for w in weekdays.all()],
                               time_begin,
                               time_end
                               ):
            raise ValidationError({
                    "weekdays": "Пересечение графика занятий!"
                })
            


@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
    pass


@admin.register(StudyStartOrder)
class StudyStartOrderAdmin(ImportExportModelAdmin):
    list_display = ["study", "datetime", "date_begin", "date_end", "teacher", "time_begin", "time_end"]
    inlines = [ActInviteStudyInline]
    form = StudyStartOrderForm


