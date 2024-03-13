from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    surname = models.CharField(max_length=100, verbose_name="Фамилия")
    last_name = models.CharField(max_length=100, verbose_name="Отчество")
    age = models.IntegerField(verbose_name="Возраст") 
    
    def fullname(self):
        return f"{self.surname} {self.name} {self.last_name}"

    def fullname_dot(self):
        return f"{self.surname[0]}. {self.name[0]}. {self.last_name}"

    def __str__(self):
        return self.fullname_dot()

    class Meta:
        verbose_name = "Человек"
        verbose_name_plural = "Люди"
