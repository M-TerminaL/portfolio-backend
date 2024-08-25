from django.shortcuts import render
from django.views import View
from .models import ProfileSetting

# Create your views here.


class MainView(View):
    def get(self, request):
        profile: ProfileSetting = ProfileSetting.objects.filter(is_main_profile=True).first()
        context = {
            'profile': profile
        }
        return render(request, 'home_module/index.html', context)

    def post(self, request):
        ...

def site_header_component(request):
    profile: ProfileSetting = ProfileSetting.objects.filter(is_main_profile=True).only('full_name').first()
    context = {
        'profile': profile
    }
    return render(request, 'shared/site_header_component.html', context)

def site_menu_navigation_component(request):
    profile: ProfileSetting = ProfileSetting.objects.filter(is_main_profile=True).first()
    context = {
        'profile': profile
    }
    return render(request, 'shared/site_menu_navigation_component.html', context)