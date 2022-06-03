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

def get_movie_details(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={config("API_KEY")}'
    return requests.get(url).json()

def you_tube_trailer(search_title):
    search_query = search_title.replace(' ', '+')
    url = f'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&q={search_query}&key={config("YOU_TUBE_API_KEY")}'
    response = requests.get(url)
    youtube_id = response.json()['items'][0]['id']['videoId']
    return youtube_id