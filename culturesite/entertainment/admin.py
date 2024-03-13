from django.contrib import admin
from person.models import Person

<<<<<<< HEAD
admin.site.register(Person)
=======
from .models import Place


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    pass
>>>>>>> 4214f858148c147eadac3574c88ede0eb22a9eac
