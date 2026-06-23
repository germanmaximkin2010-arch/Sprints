from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

from pereval.models import Pereval, User, Coords, Level, Image


class UserSerializer(WritableNestedModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'fam', 'name', 'otc', 'phone']


class CoordsSerializer(WritableNestedModelSerializer):
    class Meta:
        model = Coords
        fields = ['latitude', 'longitude', 'height']


class LevelSerializer(WritableNestedModelSerializer):
    class Meta:
        model = Level
        fields = ['winter', 'summer', 'autumn', 'spring']


class ImageSerializer(WritableNestedModelSerializer):
    class Meta:
        model = Image
        fields = ['title', 'data']


class PerevalSerializer(WritableNestedModelSerializer):
    class Meta:
        model = Pereval
        fields = [
            'beauty_title', 'title', 'other_titles', 'connect',
            'add_time', 'user', 'coords', 'level', 'status', 'images'
        ]






