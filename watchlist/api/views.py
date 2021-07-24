from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.views import APIView

from watchlist.models import WatchList
from watchlist.api.serializers import MovieSerializer, MovieModelSerializer

""" function base views """

@api_view(['GET', 'POST'])
def watch_list(request):
    """ movie list api """
    if request.method == 'GET':
        """ list """
        object_list = WatchList.objects.all()
        serialize = MovieSerializer(object_list, many=True)
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
def watch_list_details(request, pk):
    """ Movie retrive, update, delete """
    try:
        watch_list = WatchList.objects.get(pk=pk)
    except WatchList.DoesNotExist:
        return Response(
            {'error': 'Movie not found'}, status=status.HTTP_204_NO_CONTENT
        )

    if request.method == 'GET':
        serialize = MovieSerializer(watch_list)
        return Response(serialize.data)
    
    if request.method == 'PUT':
        serialize = MovieSerializer(watch_list, data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        watch_list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


""" class base views  """
class WatchListAPIView(APIView):

    def get(self, request):
        """ list """
        watch_lists = WatchList.objects.all()
        serialize = MovieModelSerializer(watch_lists, many=True)
        return Response(serialize.data)

    def post(self, request):
        serialize = MovieModelSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize.errors)   

class WatchListDetalAPIView(APIView):

    def get(self, request, pk):
        try:
            watch_list = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response(
                {'error': 'Movie not found'}, status=status.HTTP_204_NO_CONTENT)

        serialize = MovieModelSerializer(watch_list)
        return Response(serialize.data)

    def put(self, request, pk):
        try:
            watch_list = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response(
                {'error': 'Movie not found'}, status=status.HTTP_204_NO_CONTENT)

        serialize = MovieModelSerializer(watch_list, data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            watch_list = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response(
                {'error': 'Movie not found'}, status=status.HTTP_204_NO_CONTENT)

        watch_list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)