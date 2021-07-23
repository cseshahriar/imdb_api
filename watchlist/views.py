from django.shortcuts import render
from django.http import JsonResponse
from .models import Movie

def movie_list(request):
    movies = Movie.objects.all()
    data = {
        'movies': list(movies.values())
    }
    return JsonResponse(data) # py dict to json response