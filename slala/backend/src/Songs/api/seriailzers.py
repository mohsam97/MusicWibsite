from rest_framework.serializers import ModelSerializer

from Songs.models import Song, Album, Artists


class ActristSerializer(ModelSerializer):
    class Meta:
        model = Artists
        fields = '__all__'


class AlbumSerializer(ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'


class SongSerializer(ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'
