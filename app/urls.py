from django.urls import path
from .import views


app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('details/<int:movie_id>', views.details, name='details')
]
