# Generated by Django 2.0.3 on 2018-04-21 20:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20180421_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='type',
            name='add_time',
            field=models.DateField(default=datetime.datetime(2018, 4, 21, 20, 35, 18, 782043), verbose_name='添加时间'),
        ),
    ]