from django.contrib import admin
from .models import Genre, CopyRight, AvailableMarket, Artist,\
    ArtistImage, Album, AlbumImage, Track
    
# Register your models here.
admin.site.register(Genre)
admin.site.register(CopyRight)
admin.site.register(AvailableMarket)
admin.site.register(Artist)
admin.site.register(ArtistImage)
admin.site.register(Album)
admin.site.register(AlbumImage)
admin.site.register(Track)

