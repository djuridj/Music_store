# Generated by Django 3.0.8 on 2021-06-22 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_store', '0026_auto_20210622_1731'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='track_tempo',
        ),
        migrations.AddField(
            model_name='song',
            name='tempo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
