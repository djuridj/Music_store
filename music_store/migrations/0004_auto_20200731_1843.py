# Generated by Django 3.0.8 on 2020-07-31 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_store', '0003_auto_20200731_1523'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeFormat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types', models.CharField(choices=[('Vinyl', 'Vinyl'), ('CD', 'CD'), ('Cassette', 'Cassette')], max_length=50, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='typeFormat',
            field=models.ManyToManyField(to='music_store.TypeFormat'),
        ),
    ]
