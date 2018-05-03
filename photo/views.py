from django.views.generic import ListView, DetailView
from .models import Album


class AlbumList(ListView):
    queryset = Album.objects.all()
    context_object_name = 'albums'
    template_name = 'photo/album_list.html'


class AlbumDetail(DetailView):
    model = Album
    template_name = 'photo/album_detail.html'
