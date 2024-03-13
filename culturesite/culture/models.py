from django.db import models
from education.models import Study


class ArtifactOwner(models.Model):
    is_study = models.BooleanField()
    study = models.ForeignKey(Study, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return Study.objects.get(pk=self.study.id).name if self.is_study else "Культурный центр"

    class Meta:
        verbose_name = "Владелец экспоната"
        verbose_name_plural = "Владельцы экспоната"


class Artifact(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    owner = models.ForeignKey(ArtifactOwner, on_delete=models.PROTECT, verbose_name="Владелец")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Экспонат"
        verbose_name_plural = "Экспонаты"



from .signals import study_created
