# Generated by Django 3.0.8 on 2021-05-01 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_store', '0010_auto_20210429_0026'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='lyrics',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
