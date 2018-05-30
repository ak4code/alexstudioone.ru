from django.views.generic import ListView, DetailView
from .models import Album, AlbumGroup


class AlbumList(ListView):
    queryset = Album.objects.all()
    context_object_name = 'albums'
    template_name = 'photo/album_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['albumgroups'] = AlbumGroup.objects.all()
        return context


class AlbumGroupDetail(DetailView):
    model = AlbumGroup
    context_object_name = 'albumgroup'
    template_name = 'photo/album_group.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['albums'] = Album.objects.filter(group=kwargs['object'])
        return context


class AlbumDetail(DetailView):
    model = Album
    template_name = 'photo/album_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['albumgroup'] = kwargs['object'].group
        return context
