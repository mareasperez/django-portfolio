# Generated by Django 3.2.9 on 2022-02-15 03:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(verbose_name=datetime.date(2022, 2, 14)),
        ),
    ]
