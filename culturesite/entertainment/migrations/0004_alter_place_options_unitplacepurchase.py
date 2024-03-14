# Generated by Django 4.2.6 on 2024-03-14 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entertainment', '0003_FILL'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='place',
            options={'verbose_name': 'Пространство', 'verbose_name_plural': 'Пространства'},
        ),
        migrations.CreateModel(
            name='UnitPlacePurchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(verbose_name='Дата')),
                ('row', models.PositiveIntegerField(blank=True, null=True, verbose_name='Ряд')),
                ('column', models.PositiveIntegerField(blank=True, null=True, verbose_name='Место')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entertainment.event', verbose_name='Мероприятие')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='entertainment.location', verbose_name='Location')),
            ],
            options={
                'verbose_name': 'Продажа билетов на мероприятие',
                'verbose_name_plural': 'Продажа билетов на мероприятие',
            },
        ),
    ]