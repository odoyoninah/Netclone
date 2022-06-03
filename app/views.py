from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .requests import get_movies,get_movie_details, you_tube_trailer

# Create your views here.
def index(request):
    popularMovies = get_movies('popular')

    return render(request, 'index.html', {'popularMovies': popularMovies})

def details(request, movie_id):
    movie=get_movie_details(movie_id)
    youtube_id = you_tube_trailer(movie['title'])
    you_tube_url = f'https://www.youtube.com/embed/{youtube_id}?autoplay=1&muted=0'
    return render(request, 'details.html', {'movie': movie,'you_tube_url':you_tube_url})

