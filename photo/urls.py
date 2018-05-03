from django.urls import path
from .views import AlbumList, AlbumDetail

urlpatterns = [
    path('photos/', AlbumList.as_view(), name='album-list'),
    path('photos/<int:pk>/', AlbumDetail.as_view(), name='album-detail'),
]
