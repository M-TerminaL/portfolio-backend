from django.shortcuts import render
from django.views import View

from certificate_module.models import Certificate
from contact_module.forms import ContactMeForm
from contact_module.models import ContactInformation, ContactMe
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
        certificates: Certificate = Certificate.objects.filter(is_active=True).all()
        contact_info: ContactInformation = ContactInformation.objects.filter(is_active=True).first()
        contact_form = ContactMeForm()
        context = {
            'profile': profile,
            'about_me': about_me,
            'skills': skills,
            'web_apps': web_apps,
            'apps': apps,
            'certificates': certificates,
            'contact_info': contact_info,
            'contact_form': contact_form
        }
        return render(request, 'home_module/index.html', context)

    def post(self, request):
        contact_form = ContactMeForm(request.POST)
        if contact_form.is_valid():
            contact = ContactMe(
                full_name=contact_form.cleaned_data.get('full_name'),
                email=contact_form.cleaned_data.get('email'),
                subject=contact_form.cleaned_data.get('subject'),
                text=contact_form.cleaned_data.get('text')
            )
            contact.save()
            context = {
                'profile': ProfileSetting.objects.filter(is_main_profile=True).first(),
                'about_me': AboutMe.objects.filter(is_active=True).first(),
                'skills': Skill.objects.filter(is_active=True).all(),
                'web_apps': WebApplication.objects.filter(is_active=True).all(),
                'apps': App.objects.filter(is_active=True).all(),
                'certificates': Certificate.objects.filter(is_active=True).all(),
                'contact_info': ContactInformation.objects.filter(is_active=True).first(),
                'contact_form': contact_form,
                'success': 'پیام شما با موفقیت ارسال گردید.'
            }
            return render(request, 'home_module/index.html', context)

        return render(request, 'home_module/index.html', context={
            'profile': ProfileSetting.objects.filter(is_main_profile=True).first(),
            'about_me': AboutMe.objects.filter(is_active=True).first(),
            'skills': Skill.objects.filter(is_active=True).all(),
            'web_apps': WebApplication.objects.filter(is_active=True).all(),
            'apps': App.objects.filter(is_active=True).all(),
            'certificates': Certificate.objects.filter(is_active=True).all(),
            'contact_info': ContactInformation.objects.filter(is_active=True).first(),
            'contact_form': contact_form
        })


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
