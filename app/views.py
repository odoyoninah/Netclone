from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .requests import get_movies

# Create your views here.
def index(request):
    popularMovies = get_movies('popular')

    return render(request, 'index.html', {'popularMovies': popularMovies})
    