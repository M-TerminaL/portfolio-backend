from django.contrib import admin
from .models import ContactInformation, ContactMe
from jalali_date import datetime2jalali

# Register your models here.

class ContactInformationAdmin(admin.ModelAdmin):
    list_display = ['title', 'location', 'email', 'phone', 'is_active']
    list_editable = ['is_active']
    list_filter = ['is_active']


class ContactMeAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'get_created_jalali', 'is_read_by_admin']
    list_filter = ['is_read_by_admin']

    @admin.display(description='تاریخ ایجاد', ordering='created_date')
    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created_date).strftime('%a, %d %b %Y -|- %H:%M:%S')


admin.site.register(ContactInformation, ContactInformationAdmin)
admin.site.register(ContactMe, ContactMeAdmin)
