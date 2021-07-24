from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from watchlist.models import Movie
from watchlist.api.serializers import MovieSerializer


@api_view(['GET', 'POST'])
def movie_list(request):
    """ movie list api """
    if request.method == 'GET':
        """ list """
        movies = Movie.objects.all()
        serialize = MovieSerializer(movies, many=True)
        return Response(serialize.data)
    
    if request.method == 'POST':
        """ create """
        serialize = MovieSerializer(data=request.POST)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize.errors)


@api_view(['GET'])
def movie_details(request, pk):
    """ Movie details api """
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    serialize = MovieSerializer(movie)
    return Response(serialize.data)