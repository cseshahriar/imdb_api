from rest_framework import serializers
from watchlist.models import StreamPlatform, WatchList

""" serializers """
def name_length(value):
    if len(value) < 2:
        raise serializers.ValidationError('Name is too short!')

class MovieSerializer(serializers.Serializer):
    """ Movie Serializer """
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100, validators=[name_length])
    description = serializers.CharField(max_length=200)
    active = serializers.BooleanField()

    def create(self, validated_data):
        """ create """
        return WatchList.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """ update """
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance

    def validate(self, data):
        """ name and description validate """
        if data['name'] == data['description']:
            raise serializers.ValidationError('Name and Description should be different!')
        else:
            return data

    # def validate_name(self, value):
    #     """ name min length validation """
    #     if len(value) < 2:
    #         raise serializers.ValidationError('Name is too short!')
    #     else:
    #         return value


""" Model serializers """
class MovieModelSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()  # custom field 

    class Meta:
        model = WatchList
        # fields = "__all__"
        fields = ['id', 'name', 'description', 'len_name']
        # exclude = ['active']

    def get_len_name(self, object):
        """ method for len_name custom field """
        return len(object.name)

    def validate(self, data):
        """ name and description validate """
        if data['name'] == data['description']:
            raise serializers.ValidationError('Name and Description should be different!')
        else:
            return data

    def validate_name(self, value):
        """ name min length validation """
        if len(value) < 2:
            raise serializers.ValidationError('Name is too short!')
        else:
            return value
