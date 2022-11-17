from django.shortcuts import render
from django.http.response import Http404
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from rest_framework.response import Response



class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    http_method_names = ['get','post']

class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    http_method_names = ['get','post']

class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    http_method_names = ['get','post']

class PlaylistViewSet(ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    http_method_names = ['get','post']

class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    http_method_names = ['get','post']

    
    def create(self, request, *args, **kwargs):
        song_data = request.data
        # album_data = request.data
        # genre_data = genre.data

        new_song = Song.objects.create(
            title = song_data['title'],
            duration = song_data['duration'],
            plays = song_data['plays'],
         )

        new_song.save()
        
        for playlist in song_data['playlist']:
            playlist_obj = Playlist.objects.get(name=playlist['name'],)
            new_song.playlist.add(playlist_obj)

        for artist in song_data['artist']:
            artist_obj = Artist.objects.get(name=artist['artist'])
            new_song.artist.add(artist_obj)

        for album in song_data['album']:
            album_obj = Album.objects.get(name=album['album'])
            new_song.album.add(album_obj)
        
        serializer = SongSerializer(new_song)

        return Response(serializer.data)



 
