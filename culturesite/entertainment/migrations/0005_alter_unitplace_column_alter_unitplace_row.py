# Generated by Django 4.2.6 on 2024-03-14 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entertainment', '0004_alter_place_options_unitplacepurchase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unitplace',
            name='column',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Место'),
        ),
        migrations.AlterField(
            model_name='unitplace',
            name='row',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Ряд'),
        ),
    ]
