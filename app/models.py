from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_full_name(self):
        "Returns the person's full name."
        return '%s %s' % (self.first_name, self.last_name)
    full_name = property(get_full_name)

class Director(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class Actor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class Genre(models.Model):
    name = models.CharField(max_length=30)

class Movie(models.Model):
    title = models.CharField(max_length=50)
    director = models.ForeignKey(Director, related_name="movies")
    actor = models.ForeignKey(Actor, related_name="movies")
    genre = models.ForeignKey(Genre, related_name="movies")

    def average_rating(self):
        rating = sum(rating.score for rating in self.ratings)
        return rating
        
class Rating(models.Model):
    score = models.IntegerField()
    review = models.TextField(blank=True)
    movie = models.ForeignKey(Movie, related_name="ratings")
    user = models.ForeignKey(User, related_name="ratings")