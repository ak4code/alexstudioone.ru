from django.db import models


class Album(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    sort_order = models.PositiveIntegerField(default=0, db_index=True, verbose_name='Сортировка')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-sort_order']
        verbose_name_plural = 'Альбомы'
        verbose_name = 'Альбом'


class Photo(models.Model):
    file = models.ImageField(upload_to='photos/%Y/', verbose_name='')
    album = models.ForeignKey(Album, related_name='photos', blank=True, null=True, verbose_name='Альбом', on_delete=models.CASCADE)
    sort_order = models.PositiveIntegerField(default=0, db_index=True, verbose_name='Сортировка')

    def __str__(self):
        return str(self.file.url)

    class Meta:
        ordering = ['-sort_order']
        verbose_name_plural = 'Фото'
        verbose_name = 'Фотографии'
