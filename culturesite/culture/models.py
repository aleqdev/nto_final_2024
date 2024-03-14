from django.db import models
from education.models import Study


class Artifact(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    owner = models.ForeignKey(Study, on_delete=models.PROTECT, verbose_name="Владелец")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Экспонат"
        verbose_name_plural = "Экспонаты"


# Сторонние орг
class ForeignOrganization(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Сторонняя организация"
        verbose_name_plural = "Сторонние организации"


class ShowcaseType(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип выставки"
        verbose_name_plural = "Типы выставки"


class Showcase(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    type = models.ForeignKey(ShowcaseType, on_delete=models.CASCADE, verbose_name="Тип")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return f"{self.name} ({self.type})"

    class Meta:
        verbose_name = "Выставка"
        verbose_name_plural = "Выставки"
