from django.shortcuts import render
from .models import Page
from django.views.generic import TemplateView, DetailView


class Home(TemplateView):
    template_name = 'alex_site/index.html'

    def get_context_data(self, **kwargs):
        page = Page.objects.get(is_front=True)
        context = super().get_context_data(**kwargs)
        context['page'] = page
        return context


class PageDetail(DetailView):
    model = Page
    template_name = 'alex_site/page.html'
