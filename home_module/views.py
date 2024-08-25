from django.shortcuts import render
from django.views import View
from .models import ProfileSetting
from about_module.models import AboutMe, Skill
from work_module.models import WebApplication, App
# Create your views here.


class MainView(View):
    def get(self, request):
        profile: ProfileSetting = ProfileSetting.objects.filter(is_main_profile=True).first()
        about_me: AboutMe = AboutMe.objects.filter(is_active=True).first()
        skills: Skill = Skill.objects.filter(is_active=True).all()
        web_apps: WebApplication = WebApplication.objects.filter(is_active=True).all()
        apps: App = App.objects.filter(is_active=True).all()
        context = {
            'profile': profile,
            'about_me': about_me,
            'skills': skills,
            'web_apps': web_apps,
            'apps': apps
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