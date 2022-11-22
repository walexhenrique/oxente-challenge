from django.shortcuts import render
from django.views import View

from .models import Photo, Residence


class Index(View):
    def get(self, *args, **kwargs):
        residences = Residence.objects.filter(is_published=True)
        
        return render(self.request, 'residences/index.html', {'residences': residences})