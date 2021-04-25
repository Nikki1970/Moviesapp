from django.urls import path
from . import views

urlpatterns = [
    path('',views.list_movie, name="movie-list"),
    path('<slug:slug>/',views.detail_movie, name="movie-detail"),
]