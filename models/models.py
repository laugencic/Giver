from django.db import models
from django.contrib.auth.models import User

# saving movie data and genres after a user warches something
class Movie(models.Model):
    title=models.CharField(max_length=255)
    movie_id=models.PositiveIntegerField(unique=True)
        
    # genre associated with the specific movie
    genres=models.ManyToManyField(
        'Genre', blank=True
    )
    def __str__(self):
        return self.title

class Genre(models.Model):
    genre_id=models.PositiveIntegerField(unique=True)
    genre_name=models.CharField(max_length=100)

    def __str__(self):
        return self.genre_name

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    profile_picture=models.ImageField(upload_to='profile_pics/',blank=True)
    watched=models.ManyToManyField(Movie,blank=True,related_name='watched_by')
    liked=models.ManyToManyField(Movie,blank=True,related_name='liked_by')
    disliked=models.ManyToManyField(Movie,blank=True,related_name='disliked_by')
    taste=models.ManyToManyField(Genre,blank=True,related_name='preferred_by')

    def __str__(self):
        return self.user.username