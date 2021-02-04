# Generated by Django 3.0.10 on 2021-02-04 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0001_initial'),
        ('transport', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetstore',
            name='inputs',
            field=models.ManyToManyField(blank=True, to='scheduler.InputFile'),
        ),
        migrations.AlterField(
            model_name='assetstore',
            name='outputs',
            field=models.ManyToManyField(blank=True, to='scheduler.OutputFile'),
        ),
    ]
