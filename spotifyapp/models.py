from django.db import models


ARTIST_TYPE = (
    ("single", "single"),
    ("actor", "actor")
)


ALBUM_TYPE = (
    ("track", "track"),
    ("album", "album")
)

TRACK_TYPE = (
    ("track", "track"),
    ("xyz", "xyz")
)


class Genre(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        ordering = ['-name']
        
    def __str__(self):
        return f"<{self.name}>"
        
class CopyRight(models.Model):
    text = models.CharField(max_length=100)
    type = models.CharField(max_length=100)

    class Meta:
        ordering = ['-text']
        
    def __str__(self):
        return f"<{self.text}>"
        
class AvailableMarket(models.Model):
    code = models.CharField(max_length=2)
    
    class Meta:
        ordering = ['-code']
        
    def __str__(self):
        return f"<{self.code}>"
        
class Artist(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=32, choices=ARTIST_TYPE, default=ARTIST_TYPE[0][0])
    genres = models.ManyToManyField(Genre)
    popularity = models.IntegerField()
    fallowers = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-name']
        
    def __str__(self):
        return f"<{self.name}>"
         

class ArtistImage(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    height = models.IntegerField(default=640)
    width = models.IntegerField(default=640)
    

class Track(models.Model):
    name = models.CharField(max_length=100)
    label = models.CharField(max_length=100)
    type = models.CharField(max_length=15, choices=TRACK_TYPE, default=TRACK_TYPE[0][0])
    is_local = models.BooleanField(default=False)
    duration_ms = models.IntegerField()
    disc_number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']
        
    def __str__(self):
        return f"<{self.name}>"


            
class Album(models.Model):
    name = models.CharField(max_length=100)
    label = models.CharField(max_length=100)
    type = models.CharField(max_length=32, choices=ALBUM_TYPE, default=ALBUM_TYPE[0][0])
    copyright = models.ForeignKey(CopyRight, on_delete=models.CASCADE)
    upc = models.CharField(max_length=32)
    popularity = models.IntegerField()
    release_date = models.DateTimeField()
    genres = models.ManyToManyField(Genre)
    artists = models.ManyToManyField(Artist)
    tracks = models.ManyToManyField(Track)
    available_markets = models.ManyToManyField(AvailableMarket)
    release_date_precisions = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-name']
        
    def __str__(self):
        return f"<{self.name}>"
    

        
class AlbumImage(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    height = models.IntegerField(default=640)
    width = models.IntegerField(default=640)
    
        
  
