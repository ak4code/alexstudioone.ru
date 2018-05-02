from django.contrib import admin
from .models import Menu, MenuItem, Page, Card


class MenuItemInlines(admin.TabularInline):
    model = MenuItem


class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'active', 'levels',)
    search_fields = ('name',)
    list_filter = ('position',)
    inlines = (MenuItemInlines,)

    def save_model(self, request, obj, form, change):
        for item in obj.menuItems.all():
            if not item.url:
                item.url = item.get_url_page()
                item.save()
        obj.save()


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
        if not obj.owner.id:
            obj.owner = request.user
        obj.last_editor = request.user
        obj.save()


class CardAdmin(admin.ModelAdmin):
    pass


admin.site.register(Menu, MenuAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Card, CardAdmin)
