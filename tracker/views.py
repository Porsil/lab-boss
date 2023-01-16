from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Material, Batch


class Home(generic.TemplateView):
    template_name = 'index.html'


class MaterialList(generic.ListView):
    model = Material
    queryset = Material.objects.order_by('name')
    template_name = 'materials.html'
    paginate_by = 25


class BatchList(LoginRequiredMixin, generic.ListView):
    model = Batch
    queryset = Batch.objects.filter(status='To Test').order_by('-priority', 'booked_in', 'batch')
    template_name = 'tracker.html'
    paginate_by = 50