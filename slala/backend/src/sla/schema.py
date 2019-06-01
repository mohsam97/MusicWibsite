from Songs.models import Artists, Album, Song
from graphene import ObjectType, Node, Schema
from graphene_django.fields import DjangoConnectionField
from graphene_django.types import DjangoObjectType

import graphene


class ArtistsNode(DjangoObjectType):

    class Meta:
        model = Artists
        interfaces = (Node, )


class AlbumNode(DjangoObjectType):

    class Meta:
        model = Album
        interfaces = (Node, )


class SongNode(DjangoObjectType):

    class Meta:
        model = Song
        interfaces = (Node, )


class Query(graphene.ObjectType):
    artists = graphene.Field(ArtistsNode)
    all_artists = DjangoConnectionField(ArtistsNode)

    def resolve_artists(self, info):
        return Artists.objects.all()

    album = graphene.Field(AlbumNode)
    all_album = DjangoConnectionField(AlbumNode)

    def resolve_album(self, info):
        return Album.objects.all()

    song = graphene.Field(SongNode)
    all_song = DjangoConnectionField(SongNode)

    def resolve_song(self, info):
        return Song.objects.all()


schema = Schema(query=Query)
