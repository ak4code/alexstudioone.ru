from django.urls import path
from .views import AlbumList

urlpatterns = [
    path('photos/', AlbumList.as_view(), name='album-list')
]
