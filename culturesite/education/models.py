from django.db import models


class Study(models.Model):
    name = models.CharField(verbose_name="Наименование", max_length=255)
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