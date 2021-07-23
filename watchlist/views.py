from django.shortcuts import render
from django.http import JsonResponse
from .models import Movie

def movie_list(request):
    """ movie list api """
    movies = Movie.objects.all()
    data = {
        'movies': list(movies.values())
    }
    return JsonResponse(data) # py dict to json response


def movie_details(request, pk):
    """ Movie details api """
    try:
        movie = Movie.objects.get(pk=pk)
        data = {
            'name': movie.name,
            'description': movie.description,
            'active': movie.active,
        }
    except Movie.DoesNotExist:
        data = {
            'error': 'Data not from'
        }

    return JsonResponse(data)