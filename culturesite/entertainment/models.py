from django.db import models
from django.core.exceptions import ValidationError

class Place(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    capacity = models.IntegerField(verbose_name="Вместимость") 
    description = models.CharField(max_length=1000, verbose_name="Описание")
    is_location = models.BooleanField(verbose_name="Имеются-ли локации")

    def __str__(self):
        return f"{self.name} ({self.capacity} чел.)"
    
    def clean(self):
        pass
        # cnt = Location.objects.filter(place=self)
        # if (len(cnt) > 0):
        #     raise ValidationError(f"Вы не можете изменить пространство, так как у него имеются связанные локации")
        
    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Места"

class Location(models.Model):
    name = models.CharField(verbose_name="Название", max_length=255, null=True, blank=True)
    rows = models.PositiveIntegerField(verbose_name="Количество рядов")
    seats = models.PositiveIntegerField(verbose_name="Количество мест в ряду")
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name="Пространство")
    
    def __str__(self):
        return f"Локация: {self.place}. {self.rows} рядов ({self.seats} мест в ряду)"

    def clean(self):
        if (self.place.is_location == False):
            print("abacaba")
            raise ValidationError(f"Вы не можете добавить локации. У \"{self.place.name}\" не может быть локаций.")
        print(self.name, self.place.name, self.place.is_location)

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"