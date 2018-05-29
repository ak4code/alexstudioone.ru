from django.contrib import admin
from .models import Album, Photo, AlbumGroup


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1


class AlbumAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, ]


class AlbumGroupAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Album, AlbumAdmin)
admin.site.register(AlbumGroup, AlbumGroupAdmin)
