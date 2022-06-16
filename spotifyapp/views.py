from rest_framework import generics, status 
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Album, Track
from .serializers import AlbumSerializer, ReleaseDateSerializer, TrackAlbumSerializer
from .pagination import CustomPagination


class AlbumAPIView(generics.ListCreateAPIView):
    serializer_class = AlbumSerializer
    queryset = Album.objects.prefetch_related('albumimage_set').all()
    #permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    
    

class AlbumDetail(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class = AlbumSerializer
    #permission_classes = [IsAuthenticated]
    queryset = Album.objects.prefetch_related('albumimage_set').all()

    def retrieve(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        object = Album.objects.get(pk=kwargs['pk'])
        serializer = AlbumSerializer(object, many=False)
        return Response(serializer.data)
    
    def perform_destroy(self, instance):
        instance.delete()
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class TrackAPIView(generics.ListCreateAPIView):
    serializer_class = TrackAlbumSerializer
    queryset = Track.objects.prefetch_related('album_set').all()
    #permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    

class ReleaseDateAPIView(generics.ListCreateAPIView):
    serializer_class = ReleaseDateSerializer
    queryset = Album.objects.all()
    #permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination