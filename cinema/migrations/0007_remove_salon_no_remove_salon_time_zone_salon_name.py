# Generated by Django 4.2.4 on 2023-09-22 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0006_alter_movies_seans_starttime_alter_seanslar_endtime_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salon',
            name='no',
        ),
        migrations.RemoveField(
            model_name='salon',
            name='time_zone',
        ),
        migrations.AddField(
            model_name='salon',
            name='name',
            field=models.TextField(default=123),
            preserve_default=False,
        ),
    ]
