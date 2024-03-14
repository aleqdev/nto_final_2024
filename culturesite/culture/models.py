from django.db import models
from education.models import Study
from entertainment.models import Place


<<<<<<< HEAD
class Artifact(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    owner = models.ForeignKey(Study, on_delete=models.PROTECT, verbose_name="Владелец")
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Экспонат"
        verbose_name_plural = "Экспонаты"


=======
>>>>>>> 8af7a9b059f61a7d7ab000f16d0f6a98ee7fcbb9
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

class OrderExhibition(models.Model):
    dateRegister = models.DateTimeField(verbose_name="Приказ о проведении выставки")
    showcase = models.ForeignKey(Showcase, verbose_name="Выставка", on_delete=models.CASCADE)
    dateStart = models.DateTimeField(verbose_name="Дата начала проведения")
    dateEnd = models.DateTimeField(verbose_name="Дата окончания проведения")
    place = models.ForeignKey(Place, verbose_name="Место проведения", on_delete=models.CASCADE)
    artifacts = models.ManyToManyField(Artifact)

    def __str__(self):
        return f"Выставка: {self.showcase}. Место: {self.place}. Дата проведения: {self.dateStart.strftime("%Y-%m-%d %H:%M:%S")} до {self.dateEnd.strftime("%Y-%m-%d %H:%M:%S")}. Дата регистрации: {self.dateRegister.strftime("%Y-%m-%d %H:%M:%S")}"

    class Meta:
        verbose_name = "Приказ о проведении выставки"
        verbose_name_plural = "Приказы о проведении выставок"