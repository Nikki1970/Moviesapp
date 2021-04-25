from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_movie, name="movie-list"),
    path('genres/', views.GenreListView.as_view(), name="genre-list"),
    path('directors/',views.list_director,name="director-list"),
    path('director/<int:pk>/',views.detail_director,name="director-detail"),
    path('<slug:slug>/',views.detail_movie, name="movie-detail"),
]