# Generated by Django 3.1.4 on 2021-02-27 19:40

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Related',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plugin', models.CharField(db_index=True, max_length=150, verbose_name='Наименования плагина')),
                ('related_id', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Связанные',
                'verbose_name_plural': 'Связанные данные',
                'ordering': ['plugin'],
            },
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Имя')),
                ('phone', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Телефон')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('related', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='get_related', to='clients.related', verbose_name='Связь')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
                'ordering': ['-created_at'],
            },
        ),
    ]