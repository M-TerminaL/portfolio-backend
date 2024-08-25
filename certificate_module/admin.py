from django.contrib import admin
from .models import Certificate
from django.utils.html import format_html


# Register your models here.

class CertificateAdmin(admin.ModelAdmin):
    def img(self, obj):
        return format_html(f'<img src="{obj.image.url}" width="100" height="100" />')

    list_display = ['title', 'img', 'is_active']
    list_editable = ['is_active']
    list_per_page = 10
    list_filter = ['is_active']


admin.site.register(Certificate, CertificateAdmin)
