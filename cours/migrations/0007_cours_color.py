# Generated by Django 3.2 on 2021-05-01 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cours', '0006_cours_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='cours',
            name='color',
            field=models.CharField(default='alert-info', max_length=50),
            preserve_default=False,
        ),
    ]
