# Generated by Django 3.1.1 on 2020-09-13 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vuju', '0002_auto_20200913_1358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='song_tstamp',
        ),
        migrations.AddField(
            model_name='song',
            name='tstamp',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
