from audioop import reverse
from functools import total_ordering
from re import template
from django.http import JsonResponse
from django.shortcuts import render
from producers.forms import ProducerModelForm, CreatedProducerModelForm
from . import models
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .models import Producer
from django.http import JsonResponse

import producers

# Create your views here.


def index(request):
  
    return render(request, 'index.html')
       


class ProducersListView(ListView):
    model = models.Producer
    template_name = 'producers.html'
    context_object_name = 'producers'


@method_decorator(login_required(login_url='login'), name='dispatch')
class NewProducerCreateView(CreateView):
    model = models.Producer
    form_class = ProducerModelForm
    template_name = 'new_producer.html'
    sucess_url = '/producers/'


class ProducerDetailView(DetailView):
    model = models.Producer
    template_name = 'producer_detail.html'

@method_decorator(login_required(login_url='login'), name='dispatch')
class ProducerUpdateView(UpdateView):
    model = models.Producer
    form_class = CreatedProducerModelForm
    template_name = 'producer_update.html'

    def get_success_url(self):
        return reverse_lazy('producer_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required(login_url='login'), name='dispatch')
class ProducerDeleteView(DeleteView):
    model = models.Producer
    template_name = 'producer_delete.html'
    sucess_url = '/producers/'

    def get_success_url(self):
        return reverse_lazy('producers')
    
def retorna_total_area(request):
    total = Producer.objects.all().aggregate(Sum('total_area_hectares'))['total_area_hectares__sum']
    print(total)
    return JsonResponse({'total': total})

def retorna_total_arable_area(request):
    total = Producer.objects.all().aggregate(Sum('arable_area_hectares'))['arable_area_hectares__sum']
    print(total)
    return JsonResponse({'total': total})

def retorna_total_vegetation_area(request):
    total = Producer.objects.all().aggregate(Sum('vegetation_area_hectares'))['vegetation_area_hectares__sum']
    print(total)
    return JsonResponse({'total': total})

def retorna_total_prod(request):
    total = Producer.objects.all().count()
    print(total)
    return JsonResponse({'total': total})

def relatorio_estado(request):
    producers = Producer.objects.all()
    
    label = []
    data = []
    
    for producer in producers:
        qtd = Producer.objects.filter(state=producer.state).count()
        
        if producer.state not in label:
            label.append(producer.state)
            data.append(qtd)

    return JsonResponse({'labels': label , 'data': data })

def relatorio_areas_agric_veget(request):
    
    total_agric = Producer.objects.all().aggregate(Sum('arable_area_hectares'))['arable_area_hectares__sum']
    total_veget = Producer.objects.all().aggregate(Sum('vegetation_area_hectares'))['vegetation_area_hectares__sum']

    
    return JsonResponse({'total_agric': total_agric, 'total_veget': total_veget})

def relatorio_cultura(request):
    producers = Producer.objects.all()
    
    label = []
    data = []
    
    for producer in producers:
        qtd = Producer.objects.filter(planted_types=producer.planted_types).count()
    
        if producer.planted_types not in label:
            label.append(producer.planted_types)
            data.append(qtd)

    return JsonResponse({'labels': label , 'data': data })