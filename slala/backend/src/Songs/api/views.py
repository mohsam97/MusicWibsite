from rest_framework.generics import ListAPIView, RetrieveAPIView

from Songs.models import Artists, Album, Song

from .seriailzers import SongSerializer, ActristSerializer, AlbumSerializer


class SongListView (ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class SongDetailView(RetrieveAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class AlbumListView (ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class AlbumDetailView(RetrieveAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class ArtistListView (ListAPIView):
    queryset = Artists.objects.all()
    serializer_class = ActristSerializer


class ArtistDetailView(RetrieveAPIView):
    queryset = Artists.objects.all()
    serializer_class = ActristSerializer
