# Generated by Django 3.0.8 on 2021-05-01 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_store', '0016_auto_20210501_2339'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vocal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vocal', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Mixed', 'Mixed')], max_length=50, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='song',
            name='language',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='feature_artists',
            field=models.ManyToManyField(to='music_store.Artist'),
        ),
        migrations.AddField(
            model_name='song',
            name='vocal',
            field=models.ManyToManyField(to='music_store.Vocal'),
        ),
    ]