from django.db import models
from education.models import Study
from entertainment.models import Place
from django.core.exceptions import ValidationError


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
    owner_study = models.ForeignKey(Study, on_delete=models.PROTECT, verbose_name="Владелец (Студия)", null=True, blank=True, help_text="Выберите только одного владельца")
    owner_foreign_organization = models.ForeignKey(ForeignOrganization, on_delete=models.PROTECT, verbose_name="Владелец (Сторонняя организация)", null=True, blank=True, help_text="Выберите только одного владельца")

    
    def owner(self):
        if self.owner_study is not None:
            return self.owner_study
        return self.owner_foreign_organization
    def __str__(self):
        return f"Наименование: {self.name}. Владелец: {self.owner()}"
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


class ShowcaseOrder(models.Model):
    date_register = models.DateTimeField(verbose_name="Приказ о проведении выставки")
    showcase = models.ForeignKey(Showcase, verbose_name="Выставка", on_delete=models.CASCADE)
    date_start = models.DateTimeField(verbose_name="Дата начала проведения")
    date_end = models.DateTimeField(verbose_name="Дата окончания проведения")
    place = models.ForeignKey(Place, verbose_name="Место проведения", on_delete=models.CASCADE)
    artifacts = models.ManyToManyField(Artifact)

    def __str__(self):
        return f"Выставка: {self.showcase}. Место: {self.place}. Дата проведения: {self.date_start.strftime("%Y-%m-%d %H:%M:%S")} до {self.date_end.strftime("%Y-%m-%d %H:%M:%S")}. Дата регистрации: {self.date_register.strftime("%Y-%m-%d %H:%M:%S")}"

    class Meta:
        verbose_name = "Приказ о проведении выставки"
        verbose_name_plural = "Приказы о проведении выставок"


class ArtifactAquireAct(models.Model):
    date = models.DateTimeField(verbose_name="Дата")
    showcase_order = models.ForeignKey(ShowcaseOrder, on_delete=models.CASCADE, verbose_name="Приказ о проведении выставки")
    artifacts = models.ManyToManyField(Artifact, verbose_name="Экспонаты")
    
    def __str__(self):
        return f"{self.showcase_order.showcase.name}"

    def clean(self):
        print("aba", self.showcase_order.showcase.type)
        print(self.artifacts.all().all())


    class Meta:
        verbose_name = "Поступление экспонатов от сторонней организации"
        verbose_name_plural = "Поступления экспонатов от сторонней организации"


class ArtifactTransportAct(models.Model):
    date_transport = models.DateTimeField(verbose_name="Дата передачи экспоната")
    showcase_order = models.ForeignKey(ShowcaseOrder, on_delete=models.CASCADE, verbose_name="Приказ о проведении выставки")
    artifacts = models.ManyToManyField(Artifact, verbose_name="Передаваемые артифакты на выставку")
    
    def __str__(self):
        return f"{self.showcase_order.showcase.name}"

    def clean(self):
        pass
        # print("aba", self.showcase_order.showcase.type)
        # print(self.artifacts.all().all())


    class Meta:
        verbose_name = "Акт передачи экспонатов на выставку"
        verbose_name_plural = "Акты передачи экспонатов на выставки"

class ArtifactReturnAct(models.Model):
    datetime = models.DateTimeField(verbose_name="Дата")
    showcase_order = models.ForeignKey(ShowcaseOrder, on_delete=models.CASCADE, verbose_name="Приказ о проведении выставки")
    artifacts = models.ManyToManyField(Artifact, verbose_name="Экспонаты")

    def __str__(self):
        return f"{self.showcase_order.showcase.name}"

    class Meta:
        verbose_name = "Акт возврата экспонатов"
        verbose_name_plural = "Акты возврата экспонатов"

        
