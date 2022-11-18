from rest_framework import serializers
from .models import *

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'

class SongSerializer(serializers.ModelSerializer):
    # album = AlbumSerializer(many=True, required=False)
    # artist = ArtistSerializer(many=True, required=False)
    # playlist = PlaylistSerializer(many=True, required=False)
    
    class Meta:
        model = Song
        fields = ('title',
                  'duration',
                  'plays',
                  'artist',
                  'album',
                  'playlist'
        )

     
class VoodooSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()
    album = AlbumSerializer(many=True)
    artist = ArtistSerializer(many=True)
    playlist = PlaylistSerializer(many=True)
    
    class Meta:
        model = Song
        fields = '__all__'
    
    
    
    
    
    
    
    
    
    
    
    
    # def create(self, validated_data):
    #     song = Song.objects.create(**validated_data, artist=artist_instance)
    #     artists = validated_data.pop('artist')
    #     # genres = validated_data.pop('genre')

    #     # artist_instance, created = Artist.objects.create(artist=name['name'])
    #     # genre_instance, created = Genre.objects.create(genre=name['name'])


    #     for artist in artists:
    #         artist_instance, created = Artist.objects.get_or_create(name=artist['name'])
    #         song = Song.objects.add(artist_instance)
    
    #     # for genre in genres:
    #     #     genre_instance, created = Genre.objects.get_or_create(genre=name['name'])
    #     #     song = Song.objects.add(genre_instance)

    #     return song
        
        
        
        
     