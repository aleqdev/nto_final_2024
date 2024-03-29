# Generated by Django 4.2.6 on 2023-10-10 17:45

import os
import csv

from django.db import migrations


csv_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "region.csv"))


def populate(apps, schema_editor):
    Region = apps.get_model("regions", "Region")

    with open(csv_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        regions_names = set()
        cities = []

        for row in reader:
            regions_names.add(row["region_name"])
            cities.append((row["city"], row["region_name"]))

    Region.objects.using(schema_editor.connection.alias).bulk_create(
        list(map(lambda name: Region(name=name), regions_names))
    )

    City = apps.get_model("regions", "City")

    City.objects.using(schema_editor.connection.alias).bulk_create(
        list(map(lambda city: City(name=city[0], region=Region.objects.get(name=city[1])), cities))
    )


class Migration(migrations.Migration):
    dependencies = [
        ("regions", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(populate),
    ]
