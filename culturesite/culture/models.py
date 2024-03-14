from django.db import models
from education.models import Study


# Сторонние орг
class ForeignOrganization(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Сторонняя организация"
        verbose_name_plural = "Сторонние организации"


class Artifact(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    owner_study = models.ForeignKey(Study, on_delete=models.PROTECT, verbose_name="Владелец (Студия)", null=True, blank=True)
    owner_foreign_organization = models.ForeignKey(ForeignOrganization, on_delete=models.PROTECT, verbose_name="Владелец (Сторонняя организация)", null=True, blank=True)

    def __str__(self):
        return self.name
    
    def owner(self):
        if self.owner_study is not None:
            return self.owner_study
        return self.owner_foreign_organization
    owner.short_description = "Владелец"

    class Meta:
        verbose_name = "Экспонат"
        verbose_name_plural = "Экспонаты"


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


class ArtifactReturnAct(models.Model):
    datetime = models.DateTimeField(verbose_name="Дата")
    showcase_order = models.ForeignKey(verbose_name="Приказ о проведении выставки")
    artifacts = models.ManyToManyField(Artifact, on_delete=models.CASCADE, verbose_name="Экспонаты")

    def __str__(self):
        return f"{self.showcase_order.showcase.name}"

    class Meta:
        verbose_name = "Акт возврата экспонатов"
        verbose_name_plural = "Акты возврата экспонатов"
