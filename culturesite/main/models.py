from django.db import models

# class Room(models.Model):
#     name = models.CharField(verbose_name="Название", max_length=255)
#     level = models.PositiveIntegerField(verbose_name="Этаж")

# class Hotel(models.Model):
#     rooms = models.ManyToManyField(Room)

class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name="ФИО")

    def __str__(self):
        return self.name

class Book(models.Model):
   author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Автор")
   title = models.CharField(max_length=100, verbose_name="Заголовок")
   price = models.PositiveBigIntegerField(default=0, null=True, blank=True)
   def __str__(self):
    return f"Книга {self.title}. Автор {self.author}"