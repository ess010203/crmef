# Generated by Django 3.2 on 2021-06-22 23:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20210622_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
