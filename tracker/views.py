from django.shortcuts import render
from django.views import generic
from .models import Material, Batch


class Home(generic.TemplateView):
    template_name = 'index.html'


class MaterialList(generic.ListView):
    model = Material
    queryset = Material.objects.order_by('name')
    template_name = 'materials.html'
    paginate_by = 25


class BatchList(generic.ListView):
    model = Batch
    queryset = Batch.objects.filter(status='To Test').order_by('booked_in')
    template_name = 'tracker.html'
    paginate_by = 25