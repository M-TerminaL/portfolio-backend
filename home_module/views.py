from django.shortcuts import render
from django.views import View


# Create your views here.


class MainView(View):
    def get(self, request):
        return render(request, 'home_module/index.html')

    def post(self, request):
        ...

def site_header_component(request):
    return render(request, 'shared/site_header_component.html')

def site_menu_navigation_component(request):
    return render(request, 'shared/site_menu_navigation_component.html')