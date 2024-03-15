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
    
    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"


class Weekday(models.Model):
    name = models.CharField(verbose_name="Название")


class StudyStartOrder(models.Model):
    datetime = models.DateTimeField(verbose_name="Дата формирования приказа")
    study = models.ForeignKey(Study, on_delete=models.CASCADE, verbose_name="Студия")
    date_begin = models.DateField(verbose_name="Дата начала работы")
    date_end = models.DateField(verbose_name="Дата окончания работы")
    teacher = models.ForeignKey(TeacherEducation, on_delete=models.CASCADE, verbose_name="Преподаватель")
    weekdays = models.ManyToManyField(Weekday, verbose_name="Дни недели")
    time = models.TimeField(verbose_name="Время занятий")
