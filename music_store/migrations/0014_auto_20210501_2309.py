# Generated by Django 3.0.8 on 2021-05-01 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_store', '0013_auto_20210501_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='genre',
            field=models.CharField(choices=[('Rock', 'Rock'), ('HipHop', 'HipHop'), ('Electronic', 'Electronic'), ('Folk', 'Folk'), ('Reggae', 'Reggae'), ('Country', 'Country'), ('Jazz', 'Jazz'), ('Classical', 'Classical'), ('Metal', 'Metal'), ('Pop', 'Pop'), ('Punk', 'Punk')], max_length=50, null=True),
        ),
    ]
