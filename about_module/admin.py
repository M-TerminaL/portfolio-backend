from django.contrib import admin
from .models import *
# Register your models here.

class AboutMeAdmin(admin.ModelAdmin):
    list_display = ['field_of_study', 'year_of_graduation', 'is_active']
    list_editable = ['is_active']


class SkillAdmin(admin.ModelAdmin):
    list_display = ['title', 'skill_percentage', 'priority', 'is_active']
    list_editable = ['skill_percentage', 'is_active']
    list_filter = ['is_active', 'skill_percentage']
    list_per_page = 15
    search_fields = ['title']


admin.site.register(AboutMe, AboutMeAdmin)
admin.site.register(Skill, SkillAdmin)