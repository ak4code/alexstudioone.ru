from django.urls import path
from .views import AlbumList, AlbumDetail, AlbumGroupDetail

urlpatterns = [
    path('photos/', AlbumList.as_view(), name='album-list'),
    path('photos/group/<slug:slug>/', AlbumGroupDetail.as_view(), name='album-group'),
    path('photos/album/<int:pk>/', AlbumDetail.as_view(), name='album-detail'),
]
