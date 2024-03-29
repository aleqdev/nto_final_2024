# Generated by Django 4.2.6 on 2024-03-15 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=255, verbose_name='ФИО посетителя')),
            ],
            options={
                'verbose_name': 'Посетитель центра',
                'verbose_name_plural': 'Посетители центров',
            },
        ),
        migrations.CreateModel(
            name='Weekday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='StudyStartOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(verbose_name='Дата формирования приказа')),
                ('date_begin', models.DateField(verbose_name='Дата начала работы')),
                ('date_end', models.DateField(verbose_name='Дата окончания работы')),
                ('time_begin', models.TimeField(verbose_name='Время начала занятий')),
                ('time_end', models.TimeField(verbose_name='Время окончания занятий')),
                ('study', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.study', verbose_name='Студия')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.teachereducation', verbose_name='Преподаватель')),
                ('weekdays', models.ManyToManyField(to='education.weekday', verbose_name='Дни недели')),
            ],
        ),
        migrations.CreateModel(
            name='ActInviteStudy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Дата заявки')),
                ('act_study_start_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.studystartorder', verbose_name='Приказ о работе студии')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.student', verbose_name='Студент')),
            ],
            options={
                'verbose_name': 'Посетитель центра',
                'verbose_name_plural': 'Посетители центров',
            },
        ),
    ]
