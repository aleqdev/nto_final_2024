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


class EventType(models.Model):
    type_name = models.CharField(max_length=50, verbose_name="Тип мероприятия")

    def __str__(self):
        return self.type_name
    
    class Meta:
        verbose_name = "Тип мероприятия"
        verbose_name_plural = "Типы мероприятий"


class Event(models.Model):
    date = models.DateField(verbose_name="Дата проведения")
    name = models.CharField(max_length=150, verbose_name="Название")
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE, verbose_name="Тип")
    datetime_begin = models.DateTimeField(verbose_name="Время начала")
    datetime_end = models.DateTimeField(verbose_name="Время окончания")
    visitors_count = models.PositiveIntegerField(verbose_name="Количество поситителей")
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name="Пространство")
    is_paid = models.BooleanField(verbose_name="Платное мероприятие")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return f"{self.name} ({self.datetime_begin} - {self.datetime_end})"
    
    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"


class TicketPriceEvent(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name="Мероприятие")
    

    class Meta:
        verbose_name = "Установка цен на билеты"
        verbose_name_plural = "Установки цен на билеты"