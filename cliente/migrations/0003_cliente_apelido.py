# Generated by Django 3.0.8 on 2020-08-25 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_auto_20200824_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='apelido',
            field=models.CharField(blank=True, max_length=255, verbose_name='Apelido/Referência'),
        ),
    ]
