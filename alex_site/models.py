from django.conf import settings
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse
from ckeditor.fields import RichTextField


class SiteMetaBase(models.Model):
    seo_title = models.CharField(max_length=200, verbose_name='SEO Заголовок')
    seo_description = models.TextField(max_length=300, verbose_name='SEO Описание')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    class Meta:
        abstract = True


class Menu(models.Model):
    TOP = 'TOP'
    NAV = 'NAV'
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'
    FOOTER = 'FOOTER'
    POSITION_CHOICES = (
        (None, 'Не установлено'),
        (TOP, 'Верхняя панель'),
        (NAV, 'Навигация'),
        (LEFT, 'Левая панель'),
        (RIGHT, 'Правая панель'),
        (FOOTER, 'Футер'),
    )
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    position = models.CharField(max_length=10, choices=POSITION_CHOICES, default=None, verbose_name='Расположение')
    active = models.BooleanField(default=False, verbose_name='Активное')
    levels = models.PositiveSmallIntegerField(default=1, verbose_name='Уровень вложености')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['pk']
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class MenuItem(MPTTModel):
    menuId = models.ForeignKey(Menu, related_name='menuItems', on_delete=models.CASCADE, verbose_name='Меню')
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children',
                            verbose_name='Раздел')
    pageId = models.ForeignKey('Page', blank=True, null=True, related_name='menuElements', on_delete=models.CASCADE,
                               verbose_name='Страница')
    url = models.CharField(max_length=300, blank=True, null=True, verbose_name='Ссылка')
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок')

    def get_url_page(self):
        if self.pageId:
            return str(self.pageId.get_absolute_url())
        else:
            return "#"

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-order']
        verbose_name = 'Элемент меню'
        verbose_name_plural = 'Элементы меню'


class Page(SiteMetaBase):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = RichTextField(blank=True, null=True, verbose_name='Контент')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, related_name='pages',
                              on_delete=models.CASCADE, verbose_name='Владелец')
    last_editor = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, related_name='lastEditPages',
                                    on_delete=models.CASCADE, verbose_name='Последний редактор')
    slug = models.SlugField(max_length=200, blank=True, null=True, verbose_name='Короткая ссылка')
    is_front = models.BooleanField(default=False, verbose_name='Главная страница')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        if self.is_front:
            return reverse('home')
        else:
            return reverse('page', args=[str(self.slug)])

    class Meta:
        ordering = ['pk']
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'


class Card(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = RichTextField(blank=True, null=True, verbose_name='Текст')
    image = models.ImageField(upload_to='cards/', verbose_name='Картинка')
    pageId = models.ManyToManyField('Page', blank=True, related_name='cards', verbose_name='Страницы')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['pk']
        verbose_name = 'Карточка'
        verbose_name_plural = 'Карточки'