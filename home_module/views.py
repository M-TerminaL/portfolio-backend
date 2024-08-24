from django.shortcuts import render
from django.views import View


# Create your views here.


class MainView(View):
    def get(self, request):
        return render(request, 'home_module/index.html')

    def post(self, request):
        ...
