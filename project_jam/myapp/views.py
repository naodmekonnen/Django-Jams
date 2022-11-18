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
    http_method_names = ['get','post','post','delete']

class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    http_method_names = ['get','post','post','delete']

class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    http_method_names = ['get','post','post','delete']

class PlaylistViewSet(ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    http_method_names = ['get','post','post','delete']

class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    http_method_names = ['get','post','put', 'delete']

class VoodooViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = VoodooSerializer
    http_method_names = ['get']

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # def create(self, request, *args, **kwargs):
    #     song_data = request.data
    #     # album_data = request.data
    #     # genre_data = genre.data

    #     playlists = request.data.pop('playlist')
    #     artists = request.data.pop('artist')
    #     albums = request.data.pop('album')

    #     # new_song = Song.objects.create(
    #     #     title = song_data['title'],
    #     #     duration = song_data['duration'],
    #     #     plays = song_data['plays'],
    #     #  )
    #     serializer = SongSerializer(data=song_data)
    #     serializer.is_valid(raise_exception=True)
    #     new_song = serializer.save()
        
    #     for playlist in playlists:
    #         playlist_obj, created = Playlist.objects.get_or_create(name=playlist['name'])
    #         new_song.playlist.add(playlist_obj)

    #     for artist in artists:
    #         artist_obj, created = Artist.objects.get_or_create(name=artist['name'])
    #         new_song.artist.add(artist_obj)

    #     for album in albums:
    #         album_obj, created = Album.objects.get_or_create(title=album['name'])
    #         new_song.album.add(album_obj)
        

    #     return Response(serializer.data)

    # def update(self, request, *args, **kwargs):
    #     kwargs['partial'] = True
    #     return super().update(request, *args, **kwargs)







 
