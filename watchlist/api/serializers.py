from rest_framework import serializers
from watchlist.models import StreamPlatform, WatchList

""" serializers """
def name_length(value):
    if len(value) < 2:
        raise serializers.ValidationError('Name is too short!')

class MovieSerializer(serializers.Serializer):
    """ Movie Serializer """
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100, validators=[name_length])
    storyline = serializers.CharField(max_length=200)
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

    # def validate_title(self, value):
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
        fields = ['id', 'title', 'storyline', 'len_name', 'platform']
        # exclude = ['active']

    def get_len_name(self, object):
        """ method for len_name custom field """
        return len(object.title)

    def validate(self, data):
        """ name and description validate """
        if data['title'] == data['storyline']:
            raise serializers.ValidationError('title and storyline should be different!')
        else:
            return data

    def validate_title(self, value):
        """ name min length validation """
        if len(value) < 2:
            raise serializers.ValidationError('title is too short!')
        else:
            return value


class StreamPlatformSerializer(serializers.ModelSerializer):
    """ StreamPlatform Serializer """
    # StreamPlatform has many watchlist, parent -> child list
    watchlist = MovieModelSerializer(many=True, read_only=True) # nested serializers
    
    # watchlist = serializers.StringRelatedField(many=True)
    # watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # watchlist = serializers.HyperlinkedRelatedField(
    #     many=True, read_only=True, view_name='watch-detail')

    class Meta:
        model = StreamPlatform
        fields = "__all__"
