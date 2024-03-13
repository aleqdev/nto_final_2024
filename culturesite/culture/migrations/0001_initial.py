# Generated by Django 4.2.6 on 2024-03-13 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtifactOwner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_study', models.BooleanField(verbose_name='Является студией')),
                ('study', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='education.study', verbose_name='Студия')),
            ],
            options={
                'verbose_name': 'Владелец экспоната',
                'verbose_name_plural': 'Владельцы экспоната',
            },
        ),
        migrations.CreateModel(
            name='Artifact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='culture.artifactowner', verbose_name='Владелец')),
            ],
            options={
                'verbose_name': 'Экспонат',
                'verbose_name_plural': 'Экспонаты',
            },
        ),
    ]
