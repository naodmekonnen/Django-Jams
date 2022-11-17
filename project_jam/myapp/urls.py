from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'artists', ArtistViewSet)
router.register(r'albums', AlbumViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'playlists', PlaylistViewSet)
router.register(r'songs', SongViewSet)

urlpatterns = [
    path('', include(router.urls))
]