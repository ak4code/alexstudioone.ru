from photo.models import Photo
from .models import Page, Card
from django.views.generic import TemplateView, DetailView, ListView


class Home(TemplateView):
    template_name = 'alex_site/index.html'

    def get_context_data(self, **kwargs):
        page, created = Page.objects.get_or_create(is_front=True,
                                                   defaults={'title': 'Главная', 'seo_title': 'Главная',
                                                             'seo_description': 'Главная', 'slug': 'home',
                                                             'is_front': True})
        context = super().get_context_data(**kwargs)
        context['page'] = page
        context['photos'] = Photo.objects.all().order_by('?')[:10]
        return context


class PageDetail(DetailView):
    model = Page
    template_name = 'alex_site/page.html'


class PartyList(ListView):
    queryset = Card.objects.all()
    context_object_name = 'cards'
    template_name = 'alex_site/party-list.html'


class PartyDetail(DetailView):
    model = Card
    template_name = 'alex_site/party-detail.html'