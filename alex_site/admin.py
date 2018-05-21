from django.contrib import admin
from .models import Page, Card, CardPhoto, SiteConfiguration, SocialLink
from solo.admin import SingletonModelAdmin
from django.http import HttpResponseRedirect

try:
    from django.utils.encoding import force_unicode
except ImportError:
    from django.utils.encoding import force_text as force_unicode
from django.utils.translation import ugettext as _


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'last_editor', 'created', 'updated',)
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ('owner', 'last_editor', 'created', 'updated',)
    fieldsets = (
        ('Контент', {
            'classes': ('wide',),
            'fields': ('title', 'content',),
        }),
        ('SEO', {
            'classes': ('wide',),
            'fields': ('seo_title', 'seo_description', 'slug'),
        }),
        ('Мета информация', {
            'classes': ('collapse',),
            'fields': ('owner', 'last_editor', 'created', 'updated'),
        }),
    )

    def save_model(self, request, obj, form, change):
        if not obj.owner:
            obj.owner = request.user
        obj.last_editor = request.user
        obj.save()


class CardPhotoInline(admin.TabularInline):
    model = CardPhoto
    extra = 3


class CardAdmin(admin.ModelAdmin):
    inlines = (CardPhotoInline,)


class SocialLinkInline(admin.TabularInline):
    model = SocialLink
    extra = 1


class SiteAdmin(SingletonModelAdmin):
    inlines = (SocialLinkInline,)

    def response_change(self, request, obj):
        msg = _('%(obj)s изменены успешно.') % {'obj': force_unicode(obj)}
        if '_continue' in request.POST:
            self.message_user(request, msg + ' ' + _('Вы внесли изменения ниже.'))
            return HttpResponseRedirect(request.path)
        else:
            self.message_user(request, msg)
            return HttpResponseRedirect("../../")


admin.site.register(Page, PageAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(SiteConfiguration, SiteAdmin)
