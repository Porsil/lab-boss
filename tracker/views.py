from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.views.generic import UpdateView, DeleteView
from django.http import HttpResponseRedirect
from .models import Material, Batch


class Home(generic.TemplateView):
    template_name = 'index.html'


class MaterialList(LoginRequiredMixin, generic.ListView):
    model = Material
    queryset = Material.objects.order_by('status', 'name')
    template_name = 'materials.html'
    paginate_by = 25


class BatchList(LoginRequiredMixin, generic.ListView):
    model = Batch
    queryset = Batch.objects.filter(status='To Test').order_by(
        '-priority', 'booked_in', 'batch')
    template_name = 'tracker.html'
    paginate_by = 20


class UpdateMaterial(LoginRequiredMixin, UpdateView):
    model = Material
    fields = ['name', 'status']
    template_name = 'update_material.html'
    success_url = '/materials'


class DeleteMaterial(LoginRequiredMixin, DeleteView):
    model = Material
    template_name = 'delete_material.html'
    success_url = '/materials'
