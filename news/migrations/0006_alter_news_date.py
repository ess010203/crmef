# Generated by Django 3.2 on 2021-06-23 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_news_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateField(),
        ),
    ]
