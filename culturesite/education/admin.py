from django.contrib import admin
from .models import Study, TeacherEducation, StudyStartOrder
from import_export.admin import ImportExportModelAdmin
from .resources import StudiesResource
from django import forms


@admin.register(Study)
class StudyAdmin(ImportExportModelAdmin):
    list_display = ["id", "name"]
    resource_class = StudiesResource


@admin.register(TeacherEducation)
class TeacherEducationAdmin(ImportExportModelAdmin):
    pass


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
            

@admin.register(StudyStartOrder)
class StudyStartOrderAdmin(ImportExportModelAdmin):
    list_display = ["study", "datetime", "date_begin", "date_end", "teacher", "time_begin", "time_end"]
    form = StudyStartOrderForm


