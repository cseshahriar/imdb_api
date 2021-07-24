from rest_framework import serializers
from watchlist.models import Movie

class MovieSerializer(serializers.Serializer):
    """ Movie Serializer """
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=200)
    active = serializers.BooleanField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)