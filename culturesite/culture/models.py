from django.db import models


class Artifact(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    # owner = models.ForeignKey(on_delete=models.PROTECT, verbose_name="Владелец")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Экспонат"
        verbose_name_plural = "Экспонаты"


class ArtifactOwner(models.Model):
    is_study = models.BooleanField()
    name = models.CharField(max_length=50, verbose_name="Название")
    # owner = models.ForeignKey(on_delete=models.PROTECT, verbose_name="Владелец")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Экспонат"
        verbose_name_plural = "Экспонаты"
