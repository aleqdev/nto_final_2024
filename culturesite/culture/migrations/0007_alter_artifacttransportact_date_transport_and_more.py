# Generated by Django 4.2.6 on 2024-03-14 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('culture', '0006_artifacttransportact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artifacttransportact',
            name='date_transport',
            field=models.DateTimeField(verbose_name='Дата передачи экспоната'),
        ),
        migrations.CreateModel(
            name='ArtifactAquireAct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Дата')),
                ('artifacts', models.ManyToManyField(to='culture.artifact', verbose_name='Экспонаты')),
                ('showcase_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='culture.showcaseorder', verbose_name='Приказ о проведении выставки')),
            ],
            options={
                'verbose_name': 'Поступление экспонатов от сторонней организации',
                'verbose_name_plural': 'Поступления экспонатов от сторонней организации',
            },
        ),
    ]
