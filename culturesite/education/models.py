from django.db import models


class Study(models.Model):
    name = models.CharField(verbose_name="Наименование", max_length=255, unique=True)
    descrition = models.TextField(verbose_name="Описание")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Студия"
        verbose_name_plural = "Студии"
    

class TeacherEducation(models.Model):
    fio = models.CharField(verbose_name="ФИО", max_length=255)

    def __str__(self):
        return f"{self.fio}"
    
    def is_free(self, date_begin, date_end, weekdays_ids, time_begin, time_end):
        weekdays = Weekday.objects.filter(id__in=weekdays_ids)
        orders = StudyStartOrder.objects.filter(date_begin__gte=date_begin, date_end__lte=date_end, teacher=self)

        for order in orders:
            for order_weekday in order.weekdays.all():
                for weekday in weekdays:
                    if order_weekday.id == weekday.id:
                        if not (
                            (order.time_begin <= time_begin and order.time_end <= time_begin) or
                            (order.time_begin >= time_end and order.time_end >= time_end)
                        ):
                            return False
                        
        return True

    
    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"


class Weekday(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "День недели"
        verbose_name_plural = "Дни недели"


class StudyStartOrder(models.Model):
    datetime = models.DateTimeField(verbose_name="Дата формирования приказа")
    study = models.ForeignKey(Study, on_delete=models.CASCADE, verbose_name="Студия")
    date_begin = models.DateField(verbose_name="Дата начала работы")
    date_end = models.DateField(verbose_name="Дата окончания работы")
    teacher = models.ForeignKey(TeacherEducation, on_delete=models.CASCADE, verbose_name="Преподаватель")
    weekdays = models.ManyToManyField(Weekday, verbose_name="Дни недели")
    time_begin = models.TimeField(verbose_name="Время начала занятий")
    time_end = models.TimeField(verbose_name="Время окончания занятий")

    class Meta:
        verbose_name = "Приказ о работе студии"
        verbose_name_plural = "Приказы о работе студии"
