from unicodedata import name
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
AGE_CHOICES = (
    ('ALL', 'ALL'),
    ('KIDS', 'KIDS'),
    ('ADULTS', 'ADULTS'),
)



class Movie(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    id = models.CharField(max_length=255, primary_key=True)
    year = models.IntegerField()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    movies = models.ManyToManyField(Movie, related_name="watched_movies")
    name = models.CharField(max_length=255)
    age_limit = models.CharField(max_length=50,choices=AGE_CHOICES)
    id = models.CharField(max_length=255, primary_key=True)


