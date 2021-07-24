from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.views import APIView

from watchlist.models import Movie
from watchlist.api.serializers import MovieSerializer

""" function base views """

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
        serialize = MovieSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_details(request, pk):
    """ Movie retrive, update, delete """
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response(
            {'error': 'Movie not found'}, status=status.HTTP_204_NO_CONTENT
        )

    if request.method == 'GET':
        serialize = MovieSerializer(movie)
        return Response(serialize.data)
    
    if request.method == 'PUT':
        serialize = MovieSerializer(movie, data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


""" class base views  """
class MovieListAPIView(APIView):

    def get(self, request):
        """ list """
        movies = Movie.objects.all()
        serialize = MovieSerializer(movies, many=True)
        return Response(serialize.data)

    def post(self, request):
        serialize = MovieSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize.errors)   

class MovieDetalAPIView(APIView):

    def get(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response(
                {'error': 'Movie not found'}, status=status.HTTP_204_NO_CONTENT)

        serialize = MovieSerializer(movie)
        return Response(serialize.data)

    def put(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response(
                {'error': 'Movie not found'}, status=status.HTTP_204_NO_CONTENT)

        serialize = MovieSerializer(movie, data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response(
                {'error': 'Movie not found'}, status=status.HTTP_204_NO_CONTENT)

        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)