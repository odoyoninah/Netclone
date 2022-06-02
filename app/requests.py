import requests
from decouple import config

def get_movies(category):
    url = f'https://api.themoviedb.org/3/movie/{category}?api_key={config("API_KEY")}'
    response = requests.get(url)
    movies = response.json()
    movie_list=[]
    for movie in movies['results']:
        if movie['poster_path'] is not None:
            movie_list.append(movie)
    return movie_list