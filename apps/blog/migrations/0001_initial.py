# Generated by Django 3.2.9 on 2021-11-06 09:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='blog/images/')),
                ('date', models.DateField(verbose_name=datetime.date(2021, 11, 6))),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
