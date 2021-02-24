# Generated by Django 3.1.4 on 2021-02-22 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20210222_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='comment',
            field=models.TextField(blank=True, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='category',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='get_category', to='orders.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='serial',
            field=models.CharField(blank=True, max_length=150, verbose_name='Серийный'),
        ),
    ]