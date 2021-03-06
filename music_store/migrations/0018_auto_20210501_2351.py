# Generated by Django 3.0.8 on 2021-05-01 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_store', '0017_auto_20210501_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='KeyWords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key_word', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='vocal',
            name='vocal',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Mixed', 'Mixed'), ('Instrumental', 'Instrumental')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='song',
            name='key_words',
            field=models.ManyToManyField(to='music_store.KeyWords'),
        ),
    ]
