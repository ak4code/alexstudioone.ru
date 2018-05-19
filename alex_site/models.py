from django.conf import settings
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from solo.models import SingletonModel
from uuslug import uuslug


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
    slug = models.SlugField(max_length=200, blank=True, null=True, verbose_name='ЧПУ ссылка')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.title, instance=self)
        super(Card, self).save(*args, **kwargs)

    class Meta:
        ordering = ['pk']
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class SiteConfiguration(SingletonModel):
    site_name = models.CharField(max_length=255, default='Название сайта', verbose_name='Название сайта')
    site_descritpion = models.TextField(max_length=255, default='Описание сайта', verbose_name='Описание сайта')
    address = models.CharField(max_length=255, default='Адрес', verbose_name='Адрес')
    phones = models.CharField(max_length=255, default='+7 999 999-99-99', help_text='Телефоны указывать через запятую',
                              verbose_name='Телефоны')
    maintenance_mode = models.BooleanField(default=False, verbose_name='Режим обслуживания')

    def __str__(self):
        return "Настройки сайта"

    def phone_list(self):
        return self.phones.split(', ')

    class Meta:
        verbose_name = "Настройки сайта"
        verbose_name_plural = "Настройки сайта"


class SocialLink(models.Model):
    SOCIAL_CHOICES = (
        ('vk', 'Вконтакте'),
        ('odnoklassniki', 'Одноклассники'),
        ('instagram', 'Instagram'),
        ('youtube', 'YouTube'),
        ('facebook', 'Facebook'),
    )
    social = models.CharField(max_length=13, blank=True, null=True, choices=SOCIAL_CHOICES,
                              verbose_name='Социальная сеть')
    link = models.CharField(max_length=255, blank=True, null=True, verbose_name='Ссылка на соц. сеть')
    site = models.ForeignKey(SiteConfiguration, related_name='socials', on_delete=models.CASCADE)

    def __str__(self):
        return self.social

    class Meta:
        verbose_name = "Соц. сеть"
        verbose_name_plural = "Соц. сети"
