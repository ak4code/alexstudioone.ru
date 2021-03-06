from django.contrib import sitemaps
from django.urls import reverse

from alex_site.models import Page, Card
from photo.models import Album, AlbumGroup


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['home', 'album-list']

    def location(self, item):
        return reverse(item)


class PageSitemap(sitemaps.Sitemap):
    changefreq = "monthly"
    priority = 0.7

    def items(self):
        return Page.objects.all()

    def lastmod(self, obj):
        return obj.updated

class CardSitemap(sitemaps.Sitemap):
    changefreq = "monthly"
    priority = 0.7

    def items(self):
        return Card.objects.all()

    def lastmod(self, obj):
        return obj.updated

class AlbumSitemap(sitemaps.Sitemap):
    changefreq = "monthly"
    priority = 0.7

    def items(self):
        return Album.objects.all()

    def lastmod(self, obj):
        return obj.updated

class AlbumGroupSitemap(sitemaps.Sitemap):
    changefreq = "monthly"
    priority = 0.7

    def items(self):
        return AlbumGroup.objects.all()

    def lastmod(self, obj):
        return obj.updated