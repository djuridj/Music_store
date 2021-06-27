from django.db import models
from django.contrib.auth.models import User
import mutagen
import librosa

# Create your models here.

class Genre(models.Model):
    GENRE = (
        ('Rock', 'Rock'),
        ('HipHop', 'HipHop'),
        ('Electronic', 'Electronic'),
        ('Folk', 'Folk'),
        ('Reggae', 'Reggae'),
        ('Country', 'Country'),
        ('Jazz', 'Jazz'),
        ('Classical', 'Classical'),
        ('Metal', 'Metal'),
        ('Pop', 'Pop'),
        ('Punk', 'Punk'),
    )
    genre = models.CharField(max_length=50, null=True, choices=GENRE)

    def __str__(self):
        return self.genre


class TypeFormat(models.Model):
    TYPE = (
        ('Vinyl', 'Vinyl'),
        ('CD', 'CD'),
        ('Cassette', 'Cassette'),
    )
    types = models.CharField(max_length=50, null=True, choices=TYPE)

    def __str__(self):
        return self.types


class Artist(models.Model):
    name = models.CharField(max_length=200)
    biography = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to='artists/', null=True, blank=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField()
    record_label = models.CharField(max_length=100)
    album_cover = models.ImageField(upload_to='album_covers/', null=True, blank=True)
    genre = models.ManyToManyField(Genre)
    typeFormat = models.ManyToManyField(TypeFormat)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    artist = models.ForeignKey(Artist, null=True, on_delete=models.SET_NULL)

    @property
    def imageURL(self):
        try:
            url = self.album_cover.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.name + ' (' + self.artist.name + ')'


class Mood(models.Model):
    mood = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.mood

class KeyWords(models.Model):
    key_word = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.key_word

class Vocal(models.Model):
    VOCAL = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Mixed', 'Mixed'),
        ('Instrumental', 'Instrumental'),
    )
    vocal = models.CharField(max_length=50, null=True, choices=VOCAL)

    def __str__(self):
        return self.vocal


class TrackTempo(models.Model):
    TEMPO = (
        ('Fast', 'Fast'),
        ('Moderate', 'Moderate'),
        ('Multiple', 'Multiple'),
        ('Slow', 'Slow'),
        ('Very Fast', 'Very Fast'),
        ('Very Slow', ' Very Slow'),
    )
    tempo = models.CharField(max_length=50, null=True, choices=TEMPO)

    def __str__(self):
        return self.tempo

class NotableInstrument(models.Model):
    INSTRUMENT = (
        ('Accordion', 'Accordion'),
        ('Acoustic Guitar', 'Acoustic Guitar'),
        ('Acoustic Piano', 'Acoustic Piano'),
        ('Banjo', 'Banjo'),
        ('Bass', 'Bass'),
        ('Choir', ' Choir'),
        ('Clarinet', ' Clarinet'),
        ('Electric Guitar', ' Electric Guitar'),
        ('Electric Piano', ' Electric Piano'),
        ('Flute', ' Flute'),
        ('Saxophone', ' Saxophone'),
        ('Synthesiser', ' Synthesiser'),
        ('Violin', ' Violin'),
        ('Drums', ' Drums'),
    )
    instrument = models.CharField(max_length=50, null=True, choices=INSTRUMENT)

    def __str__(self):
        return self.instrument

class Song(models.Model):
    title = models.CharField(max_length=100, null=True)
    album = models.ForeignKey(Album, null=True, on_delete=models.CASCADE)
    track_number = models.IntegerField(null=True)
    feature_artists = models.ManyToManyField(Artist)   
    language = models.CharField(max_length=100,null=True)
    lyrics = models.TextField(blank=True, null=True)
    duration = models.CharField(max_length=100,blank=True,null=True)
    genre = models.ManyToManyField(Genre)
    mood = models.ManyToManyField(Mood)
    vocal = models.ManyToManyField(Vocal)
    decade = models.CharField(max_length=100,blank=True,null=True)    
    notable_instruments = models.ManyToManyField(NotableInstrument)
    audio_file = models.FileField(upload_to='audio/',blank=True, null=True)
    bitrate = models.IntegerField(null=True,blank=True)
    tempo = models.CharField(max_length=100,blank=True,null=True)
    key_words = models.ManyToManyField(KeyWords)

    @property
    def get_song_duration_in_seconds(self):
        af = self.audio_file
        audio_info = mutagen.File(af).info
        duration_seconds = int(audio_info.length)
        return duration_seconds

    @property
    def get_song_duration_desciption(self):
        sec = self.get_song_duration_in_seconds
        if sec <= 120:
            return 'less then 2 mins'
        elif sec > 120 and sec <= 240:
            return '2 to 4 mins'
        elif sec > 240 and sec <= 360:
            return '4 to 6 mins'
        else:
            return 'more then 6 mins'

    @property
    def get_era(self):
        year = self.album.year
        if year >= 1960 and year < 1970:
            return '1960s'
        elif year >= 1970 and year < 1980:
            return '1970s'
        elif year >= 1980 and year < 1990:
            return '1980s'
        elif year >= 1990 and year < 2000:
            return '1990s'
        elif year >= 2000 and year < 2010:
            return '2000s'
        elif year >= 2010 and year < 2020:
            return '2010s'
        elif year >= 2020:
            return '2020s'

    
    @property
    def get_bpm(self):
        y, sr = librosa.load(self.audio_file.path)
        tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
        return tempo

    @property
    def get_tempo(self):
        bitrate = self.bitrate
        if bitrate >= 0 and bitrate < 40:
            return 'Very Slow'
        elif bitrate >= 40 and bitrate < 70:
            return 'Slow'
        elif bitrate >= 70 and bitrate < 100:
            return 'Moderate'
        elif bitrate >= 100 and bitrate < 145:
            return 'Fast'
        else:
            return 'Very Fast'
        

    def save(self, *args, **kwargs):
          self.duration = self.get_song_duration_desciption
          self.decade = self.get_era
          self.bitrate = self.get_bpm
          self.tempo = self.get_tempo
          super(Song, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.album.artist.name + ' - ' + self.title + ' (' + self.album.name + ')'

