# Generated by Django 3.0.10 on 2020-11-24 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0006_auto_20201124_1131'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='site',
            options={'ordering': ('domain',), 'verbose_name': 'site', 'verbose_name_plural': 'sites'},
        ),
    ]