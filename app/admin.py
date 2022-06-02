from django.contrib import admin

# Register your models here.
from .models import UserProfile, Movie, Profile, Video

admin.site.register(UserProfile)
admin.site.register(Movie)

