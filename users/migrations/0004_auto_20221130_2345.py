# Generated by Django 3.2.16 on 2022-11-30 16:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20221130_2342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='votes',
        ),
        migrations.AlterField(
            model_name='question',
            name='life_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 1, 23, 45, 47, 278006), verbose_name='Время жизни'),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 30, 23, 45, 47, 278006), verbose_name='Дата'),
        ),
    ]