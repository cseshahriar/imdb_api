from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.views import APIView

from rest_framework import mixins
from rest_framework import generics

from watchlist.models import WatchList, StreamPlatform, Review
from watchlist.api.serializers import (
    MovieSerializer, MovieModelSerializer, StreamPlatformSerializer,
    ReviewSerializer
)


class StreamPlatformListAPIView(APIView):
    """ StreamPlatform list and create api """

    def get(self, request):
        object_list = StreamPlatform.objects.all()
        serialize = StreamPlatformSerializer(
            object_list,
            many=True, 
            context={'request': request}
        ) 
        # context={'request': request} is for hyperlinked_related_field
        return Response(serialize.data)

    def post(self, request):
        serialize = StreamPlatformSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)


class StreamPlatformDetailAPIView(APIView):

    def get(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_204_NO_CONTENT)

        serialize = StreamPlatformSerializer(platform)
        return Response(serialize.data)

    def put(self, request, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        serialize = MovieSerializer(platform, data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response(
                {'error': 'StreamPlatform not found'}, status=status.HTTP_204_NO_CONTENT)

        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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

""" Generic mixins """
class ReviewListCreateGenericsAPIView(
    mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        """ return reviews by watchlist """
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ReviewDetailGenericsAPIView(
    mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
    mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

""" generics Concrete View Classes """
class ReviewListGenerics(generics.ListAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        """ return reviews by watchlist """
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)

class ReviewCreateGenerics(generics.CreateAPIView):
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        watchlist = WatchList.objects.get(pk=pk)
        serializer.save(watchlist=watchlist)

class ReviewDetailGenerics(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
