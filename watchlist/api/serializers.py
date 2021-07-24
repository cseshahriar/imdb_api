from rest_framework import serializers
from watchlist.models import Movie

class MovieSerializer(serializers.Serializer):
    """ Movie Serializer """
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=200)
    active = serializers.BooleanField()

    def create(self, validated_data):
        """ create """
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """ update """
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance

    def validate_name(self, value):
        """ name field validation """
        if len(value) < 2:
            raise serializers.ValidationError('Name is too short!')
        else:
            return value