from django.urls import path
from . import views


urlpatterns = [
    path('album', views.AlbumAPIView.as_view(), name='get_albums'),
    path('album/<int:pk>', views.AlbumDetail.as_view(), name='retrive_delete_album'),
    path('track', views.TrackAPIView.as_view(), name='get_track'),
    path('realese-date', views.ReleaseDateAPIView.as_view(), name='get_realese_date'),
    
]