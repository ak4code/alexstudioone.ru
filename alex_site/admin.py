from django.contrib import admin
from .models import Page, Card


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


class CardAdmin(admin.ModelAdmin):
    pass


admin.site.register(Page, PageAdmin)
admin.site.register(Card, CardAdmin)
