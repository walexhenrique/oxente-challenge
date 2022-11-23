import requests
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.views import View

from .forms.register_residence_form import ResidenceForm
from .models import Photo, Residence


class Index(View):
    def get(self, *args, **kwargs):

        residences = Residence.objects.filter(is_published=True).order_by('-id')
        # Pegando os filtros
        
        district = self.request.GET.get('district')
        price = self.request.GET.get('price')
        city = self.request.GET.get('city')

        if district:
            residences = residences.filter(district__icontains=district)
            print(residences.query)
            print('entrei')
        
        if self.convert_price(price):
            residences = residences.filter(price__lte=price)
        
        if city:
            residences = residences.filter(city__icontains=city)
        
        return render(self.request, 'residences/index.html', {'residences': residences})
    
    def convert_price(self, price):
        try:
            price = float(price)
            return price
        except:
            return False

class ResidencesDetail(View):
    def get(self, *args, **kwargs):
        residence = get_object_or_404(Residence, slug=self.kwargs.get('slug'), is_published=True)
        key = 'AkyIf2429XZZUarwmIZIeXHsB9te9u_byrn-_qzUMiz1AU0qUuvs6oiXdj56TDUu'
        url_localization = f'http://dev.virtualearth.net/REST/v1/Locations?countryRegion=Brasil&adminDistrict=PI&locality={residence.city}&postalCode={residence.zipcode}&addressLine={residence.street}&maxResults=1&key={key}'
        
        localization = requests.get(url_localization)
        latitude = localization.json()['resourceSets'][0]['resources'][0]['geocodePoints'][0]['coordinates'][0]
        longitude = localization.json()['resourceSets'][0]['resources'][0]['geocodePoints'][0]['coordinates'][1]
        return render(self.request, 'residences/detail-residence.html', {'residence': residence, 'latitude': latitude, 'longitude': longitude})

@method_decorator(login_required, name='dispatch')
class Dashboard(View):
    def get(self, *args, **kwargs):
        residences = Residence.objects.filter(owner=self.request.user)

        return render(self.request, 'residences/dashboard.html', {'residences': residences})


@method_decorator(login_required, name='dispatch')
class ResidencesCreateView(View):
    def get(self, *args, **kwargs):
        data_session = self.request.session.get('residence')
        form = ResidenceForm(data_session)

        return render(self.request, 'residences/create-residence.html', {'form': form})
    
    def post(self, *args, **kwargs):
        POST = self.request.POST
        self.request.session['residence'] = POST

        form = ResidenceForm(POST)
        if form.is_valid():
            images = self.request.FILES.getlist('images')
            residence = Residence.objects.create(owner=self.request.user, **form.cleaned_data)

            del(self.request.session['residence'])
            
            for image in images:
                Photo.objects.create(residence=residence, image=image)
            messages.success(self.request, 'Residência criada com sucesso! lembre-se não é possível mudar as fotos dela!')
        
        return redirect('residences:dashboard')


@method_decorator(login_required, name='dispatch')
class ResidencesUpdateView(View):
    def get(self, *args, **kwargs):
        residence = get_object_or_404(Residence, slug=self.kwargs.get('slug'), owner=self.request.user)
        form = ResidenceForm(instance=residence)
        return render(self.request, 'residences/update-residence.html', {'form': form})
    
    def post(self, *args, **kwargs):
        residence = get_object_or_404(Residence, slug=self.kwargs.get('slug'), owner=self.request.user)
        form = ResidenceForm(self.request.POST, instance=residence)

        if form.is_valid():
            form.save()
            messages.success(self.request, 'Residência atualizada com sucesso!!')
            return redirect('residences:dashboard')
        
        return redirect('residences:residence-create')


@method_decorator(login_required, name='dispatch')
class ResidencesDeleteView(View):
    def get(self, *args, **kwargs):
        # checks if the residence is the user's own
        residence = get_object_or_404(Residence, slug=self.kwargs.get('slug'), owner=self.request.user)
        return render(self.request, 'residences/delete-residence.html', {'residence': residence})
    
    def post(self, *args, **kwargs):
        residence = get_object_or_404(Residence, slug=self.kwargs.get('slug'), owner=self.request.user)
        messages.success(self.request, 'Residência excluida com sucesso!')
        residence.delete()
        return redirect('residences:dashboard')

    
