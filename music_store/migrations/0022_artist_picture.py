# Generated by Django 3.0.8 on 2021-05-08 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_store', '0021_auto_20210508_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='artists/'),
        ),
    ]