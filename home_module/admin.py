from django.contrib import admin
from django.utils.html import format_html
from .models import *


# Register your models here.
class ProfileSettingAdmin(admin.ModelAdmin):
    def image(self, obj):
        return format_html(f'<img src="{obj.img_profile.url}" style="width:100px; height:100px"/>')

    list_display = ['full_name', 'image', 'is_main_profile']
    list_editable = ['is_main_profile']


admin.site.register(ProfileSetting, ProfileSettingAdmin)
