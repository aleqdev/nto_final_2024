from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    capacity = models.IntegerField(verbose_name="Вместимость") 
    description = models.CharField(max_length=1000, verbose_name="Описание")

    def __str__(self):
        return f"{self.name} ({self.capacity} чел.)"

    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Места"