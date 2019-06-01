from django.urls import path
from .views import SongListView, SongDetailView, AlbumListView, AlbumDetailView, ArtistListView, ArtistDetailView


urlpatterns = [
    path('', SongListView.as_view()),
    path('<pk>', SongDetailView.as_view()),

    path('', AlbumListView.as_view()),
    path('<pk>', AlbumDetailView.as_view()),

    path('', ArtistListView.as_view()),
    path('<pk>', ArtistDetailView.as_view())
]
