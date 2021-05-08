# Generated by Django 3.0.8 on 2021-05-01 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_store', '0015_auto_20210501_2323'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mood', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='song',
            name='genre',
            field=models.ManyToManyField(to='music_store.Genre'),
        ),
        migrations.AddField(
            model_name='song',
            name='mood',
            field=models.ManyToManyField(to='music_store.Mood'),
        ),
    ]