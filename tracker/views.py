from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic, View
from django.views.generic import CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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


class BatchList(LoginRequiredMixin, generic.ListView):
    """
    Displays the batches that have a status of To Test
    """
    model = Batch
    queryset = Batch.objects.filter(status='To Test').order_by(
        '-priority', 'booked_in', 'batch')
    template_name = 'tracker.html'
    paginate_by = 15


class PriorityBatchList(LoginRequiredMixin, generic.ListView):
    """
    Displays the batches that have the priority status
    """
    model = Batch
    queryset = Batch.objects.filter(priority='True').order_by(
        'booked_in', 'batch')
    template_name = 'priority_tracker.html'
    paginate_by = 15


class AllBatchList(LoginRequiredMixin, generic.ListView):
    """
    Displays all batches
    """
    model = Batch
    template_name = 'all_tracker.html'
    paginate_by = 15

    def get_context_data(self, **kwargs):
        """
        tracker table search filters and pagination
        code adapted from
        https://stackoverflow.com/questions/5907575/how-do-i-use-pagination-with-django-class-based-generic-listviews
        """
        context = super(AllBatchList, self).get_context_data(**kwargs) 
        all_batches = Batch.objects.all().order_by('batch')
        paginator = Paginator(all_batches, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            paginate_all_batches = paginator.page(page)
        except PageNotAnInteger:
            paginate_all_batches = paginator.page(1)
        except EmptyPage:
            paginate_all_batches = paginator.page(paginator.num_pages)
        context['all_batches'] = paginate_all_batches
        return context


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


class ToggleBatch(LoginRequiredMixin, View):
    """
    Toggles the status of a batch from priority or tracker pages
    """
    def post(self, request, pk, *args, **kwargs):
        toggle_batch = get_object_or_404(Batch, pk=pk)
        if toggle_batch.status == "To Test":
            toggle_batch.status = "Approved"
        else:
            toggle_batch.status = "To Test"
        toggle_batch.save()
        return redirect('tracker')


class ToggleBatchAll(LoginRequiredMixin, View):
    """
    Toggles the status of a batch from the all_tracker page
    """
    def post(self, request, pk, *args, **kwargs):
        toggle_batch = get_object_or_404(Batch, pk=pk)
        if toggle_batch.status == "To Test":
            toggle_batch.status = "Approved"
        else:
            toggle_batch.status = "To Test"
        toggle_batch.save()
        return redirect('all_tracker')


# Materials Page


class MaterialList(LoginRequiredMixin, generic.ListView):
    """
    Displays a list of all materials
    """
    model = Material
    queryset = Material.objects.order_by('status', 'name')
    template_name = 'materials.html'
    paginate_by = 15


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
