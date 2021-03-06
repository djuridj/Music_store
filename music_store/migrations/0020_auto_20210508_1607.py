# Generated by Django 3.0.8 on 2021-05-08 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_store', '0019_auto_20210508_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_cover',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='notableinstrument',
            name='instrument',
            field=models.CharField(choices=[('Accordion', 'Accordion'), ('Acoustic Guitar', 'Acoustic Guitar'), ('Acoustic Piano', 'Acoustic Piano'), ('Banjo', 'Banjo'), ('Bass', 'Bass'), ('Choir', ' Choir'), ('Clarinet', ' Clarinet'), ('Electric Guitar', ' Electric Guitar'), ('Electric Piano', ' Electric Piano'), ('Flute', ' Flute'), ('Saxophone', ' Saxophone'), ('Synthesiser', ' Synthesiser'), ('Violin', ' Violin'), ('Drums', ' Drums')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='audio_file',
            field=models.FileField(blank=True, null=True, upload_to='audio/'),
        ),
    ]
