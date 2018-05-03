from .models import Page
from django.views.generic import TemplateView, DetailView


class Home(TemplateView):
    template_name = 'alex_site/index.html'

    def get_context_data(self, **kwargs):
        page, created = Page.objects.get_or_create(is_front=True,
                                         defaults={'title': 'Главная', 'seo_title': 'Главная',
                                                   'seo_description': 'Главная', 'slug': 'home', 'is_front': True})
        context = super().get_context_data(**kwargs)
        context['page'] = page
        return context


class PageDetail(DetailView):
    model = Page
    template_name = 'alex_site/page.html'
