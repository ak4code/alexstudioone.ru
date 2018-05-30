from django.urls import path
from .views import AlbumList, AlbumDetail, AlbumGroupDetail

urlpatterns = [
    path('', AlbumList.as_view(), name='album-list'),
    path('group/<slug:slug>/', AlbumGroupDetail.as_view(), name='album-group'),
    path('album/<int:pk>/', AlbumDetail.as_view(), name='album-detail'),
]
