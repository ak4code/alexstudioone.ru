from django.http import JsonResponse

from photo.models import Photo
from .models import Page, Card, Message
from .forms import FeedForm
from django.views.generic import TemplateView, DetailView, ListView, FormView


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


class AjaxableResponseMixin:
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super().form_valid(form)
        if self.request.is_ajax():
            form.save()
            data = {
                'done': 'true',
                'form': form.clean()
            }
            form.send_email(self.request, data)
            return JsonResponse(data)
        else:
            return response

class FeedView(AjaxableResponseMixin, FormView):
    form_class = FeedForm
    success_url = '/'
