from django.contrib import admin
from .models import Study, TeacherEducation, StudyStartOrder, Student, ActInviteStudy, StudyStartOrderReport
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

# @admin.register(StudyStartOrder)
# class StudyStartOrderAdmin(ImportExportModelAdmin):
#     # list_display = ["object", "id", "name", "capacity"]
#     inlines = [ActInviteStudyInline]
    
#     def object(self, obj):
#         return str(obj)
    
#     object.short_description = 'Объект'

@admin.register(Study)
class StudyAdmin(ImportExportModelAdmin):
    list_display = ["id", "name"]
    inlines = [StudyStartOrderInline]
    resource_class = StudiesResource


@admin.register(TeacherEducation)
class TeacherEducationAdmin(ImportExportModelAdmin):
    pass


class FilterStudyStartOrderReportDateBegin(admin.SimpleListFilter):
    title = 'Начальная дата'
    parameter_name = 'date_begin'

    def lookups(self, request, model_admin):
        return tuple(set(
            (place.date_begin, place.date_begin)
            for place
            in StudyStartOrder.objects.all()
        ))

    def queryset(self, request, queryset):
        value = self.value()

        if value is None:
            return queryset

        return queryset.filter(date_begin__gte=value)
    

class FilterStudyStartOrderReportDateEnd(admin.SimpleListFilter):
    title = 'Конечная дата'
    parameter_name = 'date_end'

    def lookups(self, request, model_admin):
        return tuple(set(
            (place.date_begin, place.date_begin)
            for place
            in StudyStartOrder.objects.all()
        ))

    def queryset(self, request, queryset):
        value = self.value()

        if value is None:
            return queryset

        return queryset.filter(date_end__lte=value)
 


class TeacherFilter(admin.SimpleListFilter):
    title = 'Преподаватель'
    parameter_name = 'teacher'

    def lookups(self, request, model_admin):
        return tuple(set(
            (place.id, place.fio)
            for place
            in TeacherEducation.objects.all()
        ))

    def queryset(self, request, queryset):
        value = self.value()

        if value is None:
            return queryset

        return queryset.filter(teacher__id=value)
    


@admin.register(StudyStartOrderReport)
class StudyStartOrderReportAdmin(admin.ModelAdmin):
    list_filter = [FilterStudyStartOrderReportDateBegin, FilterStudyStartOrderReportDateEnd, TeacherFilter]
    list_display = ["teacher", "weekdays_s", "time_begin", "time_end"]

    def weekdays_s(self, obj):
        return ' '.join([w.name for w in obj.weekdays.all()])
    weekdays_s.short_descrition = "День недели"
    

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
    inlines = [ActInviteStudyInline]


