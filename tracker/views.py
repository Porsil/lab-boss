from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic, View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Material, Batch
from .filters import BatchFilter


# Home Page


class Home(generic.TemplateView):
    """
    Displays the home page
    """
    template_name = 'index.html'


# Contact Us Page


class ContactUs(generic.TemplateView):
    """
    Displays the contact us page
    """
    template_name = 'contact_us.html'


# Batch Tracker Pages


class BatchList(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    """
    Displays the batches that have a status of To Test
    """
    model = Batch
    queryset = Batch.objects.filter(status='To Test').order_by(
        '-priority', 'booked_in', 'batch')
    template_name = 'tracker.html'
    paginate_by = 15
    permission_required = 'tracker.view_batch'


class PriorityBatchList(
        LoginRequiredMixin,
        PermissionRequiredMixin,
        generic.ListView
            ):
    """
    Displays the batches that have the priority status
    """
    model = Batch
    queryset = Batch.objects.filter(priority='True').order_by(
        'booked_in', 'batch')
    template_name = 'priority_tracker.html'
    paginate_by = 15
    permission_required = 'tracker.view_batch'


class AllBatchList(
        LoginRequiredMixin,
        PermissionRequiredMixin,
        generic.ListView
            ):
    """
    Displays all batches
    """
    model = Batch
    queryset = Batch.objects.order_by('batch')
    template_name = 'all_tracker.html'
    paginate_by = 15
    permission_required = 'tracker.view_batch'

    def get_context_data(self, **kwargs):
        """ tracker table search filters """
        context = super().get_context_data(**kwargs)
        context['filter'] = BatchFilter(
            self.request.GET,
            queryset=Batch.objects.order_by('batch'),
        )
        return context


class AddBatch(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """
    Displays the page to add a new batch to the tracker
    """
    model = Batch
    fields = ['priority', 'batch', 'material', 'comments', 'status']
    template_name = 'add_batch.html'
    success_url = '/tracker'
    permission_required = 'tracker.add_batch'


class UpdateBatch(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """
    Displays the page to update a batch
    """
    model = Batch
    fields = ['priority', 'batch', 'material', 'comments', 'status']
    template_name = 'update_batch.html'
    success_url = '/tracker'
    permission_required = 'tracker.change_batch'


class DeleteBatch(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """
    Displays the page to confirm deletion of a batch
    """
    model = Batch
    template_name = 'delete_batch.html'
    success_url = '/tracker'
    permission_required = 'tracker.delete_batch'


class ToggleBatch(LoginRequiredMixin, PermissionRequiredMixin, View):
    """
    Toggles the status of a batch from priority or tracker pages
    """
    permission_required = 'tracker.change_batch'

    def post(self, request, pk, *args, **kwargs):
        toggle_batch = get_object_or_404(Batch, pk=pk)
        if toggle_batch.status == "To Test":
            toggle_batch.status = "Approved"
        else:
            toggle_batch.status = "To Test"
        toggle_batch.save()
        return redirect('tracker')


class ToggleBatchAll(LoginRequiredMixin, PermissionRequiredMixin, View):
    """
    Toggles the status of a batch from the all_tracker page
    """
    permission_required = 'tracker.change_batch'

    def post(self, request, pk, *args, **kwargs):
        toggle_batch = get_object_or_404(Batch, pk=pk)
        if toggle_batch.status == "To Test":
            toggle_batch.status = "Approved"
        else:
            toggle_batch.status = "To Test"
        toggle_batch.save()
        return redirect('all_tracker')


# Materials Page


class MaterialList(
        LoginRequiredMixin,
        PermissionRequiredMixin,
        generic.ListView
        ):
    """
    Displays a list of all materials
    """
    model = Material
    queryset = Material.objects.order_by('status', 'name')
    template_name = 'materials.html'
    paginate_by = 15
    permission_required = 'tracker.view_material'


class AddMaterial(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """
    Displays the page to add a new material to the list
    """
    model = Material
    fields = ['name', 'status']
    template_name = 'add_material.html'
    success_url = '/materials'
    permission_required = 'tracker.add_material'


class UpdateMaterial(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """
    Displays the page to update a material
    """
    model = Material
    fields = ['name', 'status']
    template_name = 'update_material.html'
    success_url = '/materials'
    permission_required = 'tracker.change_material'


class DeleteMaterial(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """
    Displays the page to confirm deletion of a material
    """
    model = Material
    template_name = 'delete_material.html'
    success_url = '/materials'
    permission_required = 'tracker.delete_material'


class ToggleMaterial(LoginRequiredMixin, PermissionRequiredMixin, View):
    """
    Toggles the status of a material
    """
    permission_required = 'tracker.change_material'

    def post(self, request, pk, *args, **kwargs):
        toggle_material = get_object_or_404(Material, pk=pk)
        if toggle_material.status == "Active":
            toggle_material.status = "Inactive"
        else:
            toggle_material.status = "Active"
        toggle_material.save()
        return redirect('materials')
