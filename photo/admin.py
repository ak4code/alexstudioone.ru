from django.contrib import admin
from .models import Album, Photo, Video, AlbumGroup


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 3

class VideoInline(admin.TabularInline):
    model = Video
    extra = 1

class AlbumAdmin(admin.ModelAdmin):
    inlines = (PhotoInline, VideoInline)


class AlbumGroupAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Album, AlbumAdmin)
admin.site.register(AlbumGroup, AlbumGroupAdmin)
