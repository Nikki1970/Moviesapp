from django.shortcuts import render, get_object_or_404
from Moviesapp.models import Movie, Genre, Director, Studio
from django.views import generic
# Create your views here.

def list_movie(request):
    movie = Movie.objects.all()
    context = {
        'movies' : movie
    }
    return render(request,'Moviesapp/movie_list.html', context=context)


def detail_movie(request, slug):
    movie = get_object_or_404(Movie, slug=slug)
    context = {
        'movie':movie
    }
    return render(request,'Moviesapp/movie_detail.html', context=context)


class GenreListView(generic.ListView):
    model = Genre

def list_director(request):
    director = Director.objects.all()
    context = {
        'directors' : director 
    }
    return render(request, 'Moviesapp/director_list.html', context=context)


def detail_director(request, pk):
    director = get_object_or_404(Director, id=pk)
    context = {
        'director' : director
    }
    return render(request, 'Moviesapp/director_detail.html', context=context)


class StudioListView(generic.ListView):
    model = Studio
    template = "Moviesapp/studio_list.html"


def detail_studio(request, slug):
    studio = get_object_or_404(Studio, slug=slug)
    context = {
        'studio' : studio
    }
    return render(request, 'Moviesapp/studio_detail.html', context=context)