from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View

from .forms.register_residence_form import ResidenceForm
from .models import Photo, Residence


class Index(View):
    def get(self, *args, **kwargs):

        residences = Residence.objects.filter(is_published=True, **self.request.GET)
        
        return render(self.request, 'residences/index.html', {'residences': residences})

class ResidencesDetail(View):
    def get(self, *args, **kwargs):
        residence = get_object_or_404(Residence, slug=self.kwargs.get('slug'), is_published=True)
        return render(self.request, 'residences/detail-residence.html', {'residence': residence})

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
                photo = Photo.objects.create(residence=residence, image=image)
        
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
            return redirect('residences:dashboard')
        
        return redirect('residences:residence-create')


@method_decorator(login_required, name='dispatch')
class ResidencesDeleteView(View):
    def get(self, *args, **kwargs):
        # checks if the residence is the user's own
        residence = get_object_or_404(Residence, slug=self.kwargs.get('slug'), owner=self.request.user)
        return render(self.request, 'residences/delete-residence.html', {'residence': residence})
    
    def post(self, *args, **kwargs):
        # messages.success(self.request, 'Residence excluida com sucesso')
        residence = get_object_or_404(Residence, slug=self.kwargs.get('slug'), owner=self.request.user)
        residence.delete()
        return redirect('residences:dashboard')

    
