from django.contrib import admin
from django.utils.html import format_html
from .models import WebApplication, App


# Register your models here.


class WebApplicationAdmin(admin.ModelAdmin):
    def site_image(self, obj):
        return format_html(f'<img src="{obj.image.url}" width="100" height="100" />')

    list_display = ['title', 'site_image', 'is_active']
    list_editable = ['is_active']
    list_per_page = 10
    list_filter = ['is_active']


class AppAdmin(admin.ModelAdmin):
    list_display = ['title', 'program_language', 'is_active']
    list_editable = ['is_active']
    list_per_page = 10
    list_filter = ['is_active']


admin.site.register(WebApplication, WebApplicationAdmin)
admin.site.register(App, AppAdmin)
