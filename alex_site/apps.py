from django.apps import AppConfig



class AlexSiteConfig(AppConfig):
    name = 'alex_site'
    verbose_name = 'Сайт'

    def ready(self):
        from .models import SiteConfiguration
        config = SiteConfiguration.get_solo()
