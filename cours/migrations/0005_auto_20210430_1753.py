# Generated by Django 3.2 on 2021-04-30 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cours', '0004_cours_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=50)),
                ('catImage', models.ImageField(upload_to='category/')),
            ],
        ),
        migrations.AlterField(
            model_name='coursimage',
            name='CImage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='cours.cours'),
        ),
    ]
