from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Субъект РФ"
        verbose_name_plural = "Субъекты РФ"
