from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'frontpage/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['alex'] = 'ALEX STUDIO'
        return context
