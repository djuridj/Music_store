from django.db import models
from django.contrib.auth.models import User

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

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField()
    record_label = models.CharField(max_length=100)
    album_cover = models.ImageField(null=True, blank=True)
    genre = models.ManyToManyField(Genre)
    typeFormat = models.ManyToManyField(TypeFormat)
    #in_stock = models.IntegerField(default=0, blank=True, null=True)
    #avaliable = models.BooleanField(default=True, blank=True, null=True)
    #number_of_ratings = models.IntegerField(default=0)
    #average_rating = models.FloatField(default=0.0, blank=True, null=True)
    price = models.FloatField(default=0.0)
    artist = models.ForeignKey(Artist, null=True, on_delete=models.SET_NULL)

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

class Song(models.Model):
    title = models.CharField(max_length=100, null=True)
    album = models.ForeignKey(Album, null=True, on_delete=models.SET_NULL)
    track_number = models.IntegerField(null=True)
    feature_artists = models.ManyToManyField(Artist)
    
    lyrics = models.TextField(blank=True, null=True)
    duration = models.CharField(max_length=100, null=True)
    genre = models.ManyToManyField(Genre)
    mood = models.ManyToManyField(Mood)
    vocal = models.ManyToManyField(Vocal)
    language = models.CharField(max_length=100, null=True)
    key_words = models.ManyToManyField(KeyWords)

    def __str__(self):
        return self.album.artist.name + ' - ' + self.title + ' (' + self.album.name + ')'