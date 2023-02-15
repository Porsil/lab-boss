from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic, View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
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


# FilteredListView to allow pagination and filters


class FilteredListView(ListView):
    """
    Code taken from https://www.caktusgroup.com/blog/2018/10/18/
    filtering-and-pagination-django/
    """
    filterset_class = None

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = self.filterset_class(self.request.GET,
                                              queryset=queryset)
        return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


# Batch Tracker Pages


class BatchList(
        LoginRequiredMixin,
        PermissionRequiredMixin,
        generic.ListView
            ):
    """
    Displays the batches that have a status of To Test
    """
    model = Batch
    queryset = Batch.objects.filter(status='To Test').order_by(
        '-priority', 'booked_in', 'batch')
    template_name = 'tracker.html'
    paginate_by = 18
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
        FilteredListView
            ):
    """
    Displays all batches.
    FilteredListView & filterset_class added from
    https://www.caktusgroup.com/blog/2018/10/18/
    filtering-and-pagination-django/
    """
    model = Batch
    queryset = Batch.objects.order_by('batch')
    template_name = 'all_tracker.html'
    paginate_by = 20
    permission_required = 'tracker.view_batch'
    filterset_class = BatchFilter


class AddBatch(
        LoginRequiredMixin,
        PermissionRequiredMixin,
        SuccessMessageMixin,
        CreateView
            ):
    """
    Displays the page to add a new batch to the tracker
    """
    model = Batch
    fields = ['priority', 'batch', 'material', 'comments', 'status']
    template_name = 'add_batch.html'
    success_url = '/tracker'
    permission_required = 'tracker.add_batch'
    success_message = "%(batch)s added successfully"


class UpdateBatch(
        LoginRequiredMixin,
        PermissionRequiredMixin,
        SuccessMessageMixin,
        UpdateView
            ):
    """
    Displays the page to update a batch
    """
    model = Batch
    fields = ['priority', 'batch', 'material', 'comments', 'status']
    template_name = 'update_batch.html'
    success_url = '/tracker'
    permission_required = 'tracker.change_batch'
    success_message = "%(batch)s updated successfully"


class DeleteBatch(
        LoginRequiredMixin,
        PermissionRequiredMixin,
        DeleteView
            ):
    """
    Displays the page to confirm deletion of a batch
    """
    model = Batch
    template_name = 'delete_batch.html'
    success_url = '/tracker'
    permission_required = 'tracker.delete_batch'
    success_message = "%(batch)s deleted successfully"

    def delete(self, request, *args, **kwargs):
        """
        Display success message
        Adapted from: https://stackoverflow.com/questions/24822509/
        success-message-in-deleteview-not-shown
        """
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(DeleteBatch, self).delete(request, *args, **kwargs)


class ToggleBatch(
        LoginRequiredMixin,
        PermissionRequiredMixin,
        View
            ):
    """
    Toggles the status of a batch from priority or tracker pages
    """
    permission_required = 'tracker.change_batch'

    def post(self, request, pk, *args, **kwargs):
        toggle_batch = get_object_or_404(Batch, pk=pk)
        if toggle_batch.status == "To Test":
            toggle_batch.status = "Approved"
            messages.success(self.request,
                             "Batch approved successfully")
        toggle_batch.save()
        return redirect('tracker')


class ToggleBatchAll(
        LoginRequiredMixin,
        PermissionRequiredMixin,
        View
            ):
    """
    Toggles the status of a batch from the all_tracker page
    """
    permission_required = 'tracker.change_batch'

    def post(self, request, pk, *args, **kwargs):
        toggle_batch = get_object_or_404(Batch, pk=pk)
        if toggle_batch.status == "To Test":
            toggle_batch.status = "Approved"
            messages.success(self.request, "Batch approved successfully")
        else:
            toggle_batch.status = "To Test"
            messages.success(self.request,
                             "Batch status changed to To Test successfully")
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


class AddMaterial(
        LoginRequiredMixin,
        PermissionRequiredMixin,
        SuccessMessageMixin,
        CreateView
            ):
    """
    Displays the page to add a new material to the list
    """
    model = Material
    fields = ['name', 'status']
    template_name = 'add_material.html'
    success_url = '/materials'
    permission_required = 'tracker.add_material'
    success_message = "%(name)s added successfully"


class UpdateMaterial(
        LoginRequiredMixin,
        PermissionRequiredMixin,
        SuccessMessageMixin,
        UpdateView
            ):
    """
    Displays the page to update a material
    """
    model = Material
    fields = ['name', 'status']
    template_name = 'update_material.html'
    success_url = '/materials'
    permission_required = 'tracker.change_material'
    success_message = "%(name)s updated successfully"


class DeleteMaterial(
        LoginRequiredMixin,
        PermissionRequiredMixin,
        DeleteView
            ):
    """
    Displays the page to confirm deletion of a material
    """
    model = Material
    template_name = 'delete_material.html'
    success_url = '/materials'
    permission_required = 'tracker.delete_material'
    success_message = "%(name)s deleted successfully"

    def delete(self, request, *args, **kwargs):
        """
        Display success message
        Adapted from: https://stackoverflow.com/questions/24822509/
        success-message-in-deleteview-not-shown
        """
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(DeleteMaterial, self).delete(request, *args, **kwargs)


class ToggleMaterial(
        LoginRequiredMixin,
        PermissionRequiredMixin,
        View
            ):
    """
    Toggles the status of a material
    """
    permission_required = 'tracker.change_material'

    def post(self, request, pk, *args, **kwargs):
        toggle_material = get_object_or_404(Material, pk=pk)
        if toggle_material.status == "Active":
            toggle_material.status = "Inactive"
            messages.success(
                self.request,
                "Material status changed to Inactive successfully"
                    )
        else:
            toggle_material.status = "Active"
            messages.success(self.request,
                             "Material status changed to Active successfully")
        toggle_material.save()
        return redirect('materials')
