from django.template.context_processors import request
from alex_site.models import Menu


def top_menu(request):
    menu, created = Menu.objects.get_or_create(position='TOP', active=True,
                                               defaults={'active': True, 'position': 'TOP', 'name': 'Верхнее меню'})
    return {'top_menu': menu}
