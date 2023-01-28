from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic, View
from django.views.generic import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from .models import Material, Batch


# Home Page

class Home(generic.TemplateView):
    """
    Displays the home page
    """
    template_name = 'index.html'


# Batch Tracker Pages

class BatchList(LoginRequiredMixin, generic.ListView):
    """
    Displays the batches that have a status of To Test
    """
    model = Batch
    queryset = Batch.objects.filter(status='To Test').order_by(
        '-priority', 'booked_in', 'batch')
    template_name = 'tracker.html'
    paginate_by = 20


class AddBatch(LoginRequiredMixin, CreateView):
    """
    Displays the page to add a new batch to the tracker
    """
    model = Batch
    fields = ['priority', 'batch', 'material', 'comments', 'status']
    template_name = 'add_batch.html'
    success_url = '/tracker'


class UpdateBatch(LoginRequiredMixin, UpdateView):
    """
    Displays the page to update a batch
    """
    model = Batch
    fields = ['priority', 'batch', 'material', 'comments', 'status']
    template_name = 'update_batch.html'
    success_url = '/tracker'


class DeleteBatch(LoginRequiredMixin, DeleteView):
    """
    Displays the page to confirm deletion of a batch
    """
    model = Batch
    template_name = 'delete_batch.html'
    success_url = '/tracker'


# Materials Page

class MaterialList(LoginRequiredMixin, generic.ListView):
    """
    Displays a list of all materials
    """
    model = Material
    queryset = Material.objects.order_by('status', 'name')
    template_name = 'materials.html'
    paginate_by = 20


class AddMaterial(LoginRequiredMixin, CreateView):
    """
    Displays the page to add a new material to the list
    """
    model = Material
    fields = ['name', 'status']
    template_name = 'add_material.html'
    success_url = '/materials'


class UpdateMaterial(LoginRequiredMixin, UpdateView):
    """
    Displays the page to update a material
    """
    model = Material
    fields = ['name', 'status']
    template_name = 'update_material.html'
    success_url = '/materials'


class DeleteMaterial(LoginRequiredMixin, DeleteView):
    """
    Displays the page to confirm deletion of a material
    """
    model = Material
    template_name = 'delete_material.html'
    success_url = '/materials'


class ToggleMaterial(LoginRequiredMixin, View):
    """
    Toggles the status of a material
    """
    def post(self, request, pk, *args, **kwargs):
        toggle_material = get_object_or_404(Material, pk=pk)
        if toggle_material.status == "Active":
            toggle_material.status = "Inactive"
        else:
            toggle_material.status = "Active"
        toggle_material.save()
        return redirect('materials')
