from django.shortcuts import render
from Moviesapp.models import Movie, Genre, Director, Studio
from django.views import generic
# Create your views here.

def list_movie(request):
    movie = Movie.objects.all()
    context = {
        'movies' : movie
    }
    return render(request,'Moviesapp/movie_list.html', context= context)