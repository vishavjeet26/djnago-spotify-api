from rest_framework import serializers

from .models import Genre, CopyRight, AvailableMarket, Artist,\
    ArtistImage, Album, AlbumImage, Track


class CopyRightSerializer(serializers.ModelSerializer): 

    class Meta:
        model = CopyRight
        fields = ('text', 'type')
        

class GenreSerializer(serializers.ModelSerializer): 

    class Meta:
        model = Genre
        fields = ('name',)
        
class AvailableMarketsSerializer(serializers.ModelSerializer): 

    class Meta:
        model = AvailableMarket
        fields = ('code',)
        

    
class ArtistSerializer(serializers.ModelSerializer): 

    class Meta:
        model = Artist
        fields = ('name','type', 'genres', 'popularity', 'fallowers')
        


class AlbumImageSerializer(serializers.ModelSerializer): 

    class Meta:
        model = AlbumImage
        fields = ('image','height', 'width')
        
class TrackSerializer(serializers.ModelSerializer): 

    class Meta:
        model = Track
        fields = ('name','label', 'type', 'is_local', 'duration_ms', 'disc_number')        
    
        
class AlbumSerializer(serializers.ModelSerializer): 
    copyright = CopyRightSerializer(many=False)
    genres = GenreSerializer(many=True)
    artists = ArtistSerializer(many=True)
    available_markets = AvailableMarketsSerializer(many=True)
    images = AlbumImageSerializer(source='albumimage_set', many=True)
    tracks = TrackSerializer(many=True)

    
    class Meta:
        model = Album
        fields = ( 'type', 'artists', 'available_markets',  'copyright', 'genres', 'tracks',
                  'upc', 'popularity', 'release_date', 'release_date_precisions', 'images', 'id', 'name', 'label')
        
        
class AlbumTrackSerializer(serializers.ModelSerializer): 
    copyright = CopyRightSerializer(many=False)
    genres = GenreSerializer(many=True)
    artists = ArtistSerializer(many=True)
    available_markets = AvailableMarketsSerializer(many=True)
    images = AlbumImageSerializer(source='albumimage_set', many=True)

    
    class Meta:
        model = Album
        fields = ( 'type', 'artists', 'available_markets',  'copyright', 'genres', 
                  'upc', 'popularity', 'release_date', 'release_date_precisions', 'images', 'id', 'name', 'label')
        

class TrackAlbumSerializer(serializers.ModelSerializer):
    albums = AlbumTrackSerializer(source='album_set', many=True)

    class Meta:
        model = Track
        fields = ('name','label', 'type', 'is_local', 'duration_ms', 'disc_number', 'albums')
        

class ReleaseDateSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Album
        fields = (  'release_date', 'release_date_precisions', 'name', 'label')

