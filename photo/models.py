from django.db import models
from ckeditor.fields import RichTextField
from embed_video.fields import EmbedVideoField


class PhotoBase(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated = models.DateTimeField(auto_now=True, verbose_name='Изменено')
    seo_title = models.CharField(max_length=255, blank=True, null=True, verbose_name='SEO заголовок')
    seo_short_desc = models.TextField(max_length=255, blank=True, null=True, verbose_name='SEO описание')

    class Meta:
        abstract = True


class AlbumGroup(PhotoBase):
    name = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='ЧПУ ссылка')
    sort_order = models.PositiveIntegerField(default=0, db_index=True, verbose_name='Сортировка')

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('album-group', args=[str(self.slug)])

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-sort_order']
        verbose_name_plural = 'Группы альбомов'
        verbose_name = 'Группа альбома'


class Album(PhotoBase):
    title = models.CharField(max_length=200, verbose_name='Название')
    group = models.ForeignKey(AlbumGroup, related_name='albums', null=True, on_delete=models.SET_NULL,
                              verbose_name='Группа')
    content = RichTextField(blank=True, null=True, verbose_name='Контент')
    sort_order = models.PositiveIntegerField(default=0, db_index=True, verbose_name='Сортировка')
    pic = models.ImageField(upload_to='albums/', blank=True, null=True, verbose_name='Обложка')
    show_home = models.BooleanField(default=False, verbose_name='Показывать на главной')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('album-detail', args=[str(self.id)])

    class Meta:
        ordering = ['-sort_order']
        verbose_name_plural = 'Альбомы'
        verbose_name = 'Альбом'


class Photo(models.Model):
    file = models.ImageField(upload_to='photos/%Y/', verbose_name='Файл')
    album = models.ForeignKey(Album, related_name='photos', blank=True, null=True, verbose_name='Альбом',
                              on_delete=models.CASCADE)
    sort_order = models.PositiveIntegerField(default=0, db_index=True, verbose_name='Сортировка')

    def __str__(self):
        return str(self.file.url)

    class Meta:
        ordering = ['-sort_order']
        verbose_name_plural = 'Фотографии'
        verbose_name = 'Фото'


class Video(models.Model):
    link = EmbedVideoField(verbose_name='Ссылка на видео')
    album = models.ForeignKey(Album, related_name='videos', blank=True, null=True, verbose_name='Альбом',
                              on_delete=models.CASCADE)
    sort_order = models.PositiveIntegerField(default=0, db_index=True, verbose_name='Сортировка')

    def __str__(self):
        return self.link

    class Meta:
        ordering = ['-sort_order']
        verbose_name_plural = 'Видео'
        verbose_name = 'Видео'
