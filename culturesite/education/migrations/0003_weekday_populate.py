# Generated by Django 4.2.6 on 2024-03-14 11:34

from django.db import migrations, models
import django.db.models.deletion
import datetime

def populate(apps, schema_editor):
    Weekday = apps.get_model('education', 'Weekday')
    Weekday.objects.create(name="Понедельник")
    Weekday.objects.create(name="Вторник")
    Weekday.objects.create(name="Среда")
    Weekday.objects.create(name="Четверг")
    Weekday.objects.create(name="Пятница")
    Weekday.objects.create(name="Суббота")
    Weekday.objects.create(name="Воскресенье")


class Migration(migrations.Migration):
    dependencies = [
        ("education", "0002_dep")
    ]

    operations = [
        migrations.RunPython(populate, migrations.RunPython.noop)
    ]
