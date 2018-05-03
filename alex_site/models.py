from django.conf import settings
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


class SiteMetaBase(models.Model):
    seo_title = models.CharField(max_length=200, verbose_name='SEO Заголовок')
    seo_description = models.TextField(max_length=300, verbose_name='SEO Описание')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    class Meta:
        abstract = True


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
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"


class Card(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = RichTextField(blank=True, null=True, verbose_name='Текст')
    image = models.ImageField(upload_to='cards/', verbose_name='Картинка')
    pageId = models.ManyToManyField('Page', blank=True, related_name='cards', verbose_name='Страницы')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['pk']
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
