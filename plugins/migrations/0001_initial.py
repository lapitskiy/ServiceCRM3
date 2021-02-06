# Generated by Django 3.1.4 on 2021-02-05 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PluginsCrm3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен')),
                ('imp_name', models.CharField(max_length=150, verbose_name='Системное название')),
                ('version', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Плагин',
                'verbose_name_plural': 'Плагины',
                'ordering': ['title'],
            },
        ),
    ]
