from turtle import title
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
AGE_CHOICES = (
    ('ALL', 'ALL'),
    ('KIDS', 'KIDS'),
    ('ADULTS', 'ADULTS'),
)
genre = (
    ('Action', 'Action'),
    ('Horror', 'Horror'),
    ('Animation', 'Animation'),
    ('Comedy', 'Comedy'),
    ('Family', 'Family'),
)

STATUS_CHOICES = (
    ('Recently Added', 'Recently Added'),
    ('Most Watched', 'Most Watched'),
    ('Top Rated', 'Top Rated'),
)




class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age_group = models.CharField(max_length=10, choices=AGE_CHOICES, default='ALL')


class Movie(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    id = models.CharField(max_length=255, primary_key=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    genre = models.CharField(max_length=255, blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES)
    


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    movies = models.ManyToManyField(Movie, related_name="watched_movies")
    name = models.CharField(max_length=255)
    age_limit = models.CharField(max_length=50,choices=AGE_CHOICES)
    id = models.CharField(max_length=255, primary_key=True)

class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    id = models.CharField(max_length=255, primary_key=True)


