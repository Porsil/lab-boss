from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic, View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .forms import WorkloadForm
from .models import Workload, Analyst, Test
from .filters import WorkloadFilter, AllWorkloadFilter


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


# Scheduler Page


class WorkloadList(
        LoginRequiredMixin,
        PermissionRequiredMixin,
        FilteredListView
            ):
    """
    Displays the workload cards that have a status of To Do
    FilteredListView & filterset_class added from
    https://www.caktusgroup.com/blog/2018/10/18/
    filtering-and-pagination-django/
    """
    model = Workload
    queryset = Workload.objects.filter(status='To Do').order_by('-test_date',
                                                                'analyst')
    template_name = 'scheduler.html'
    paginate_by = 12
    permission_required = 'scheduler.view_workload'
    filterset_class = WorkloadFilter

    def get_context_data(self, **kwargs):
        """ card table search filters """
        context = super().get_context_data(**kwargs)
        context['filter'] = WorkloadFilter(self.request.GET,
                                           queryset=Workload.objects.order_by(
                                            'test_date'), )
        return context


class AllWorkloadList(
        LoginRequiredMixin,
        PermissionRequiredMixin,
        FilteredListView
            ):
    """
    Displays all workload cards
    FilteredListView & filterset_class added from
    https://www.caktusgroup.com/blog/2018/10/18/
    filtering-and-pagination-django/
    """
    model = Workload
    queryset = Workload.objects.order_by('-test_date', 'analyst')
    template_name = 'all_scheduler.html'
    paginate_by = 12
    permission_required = 'scheduler.view_workload'
    filterset_class = AllWorkloadFilter

    def get_context_data(self, **kwargs):
        """ card search filters """
        context = super().get_context_data(**kwargs)
        context['filter'] = AllWorkloadFilter(
            self.request.GET,
            queryset=Workload.objects.order_by('-test_date'),
        )
        return context


class AddWorkload(
        LoginRequiredMixin,
        PermissionRequiredMixin,
        SuccessMessageMixin,
        CreateView
            ):
    """
    Displays the page to add a new workload card
    """
    model = Workload
    form_class = WorkloadForm
    template_name = 'add_workload.html'
    success_url = '/scheduler'
    permission_required = 'scheduler.add_workload'
    success_message = "Card created successfully"


class UpdateWorkload(
        LoginRequiredMixin,
        PermissionRequiredMixin,
        SuccessMessageMixin,
        UpdateView
            ):
    """
    Displays the page to update a workload card
    """
    model = Workload
    form_class = WorkloadForm
    template_name = 'update_workload.html'
    success_url = '/scheduler'
    permission_required = 'scheduler.change_workload'
    success_message = "Card updated successfully"


class DeleteWorkload(
        LoginRequiredMixin,
        PermissionRequiredMixin,
        DeleteView
            ):
    """
    Displays the page to confirm deletion of a workload card
    """
    model = Workload
    template_name = 'delete_workload.html'
    success_url = '/scheduler'
    permission_required = 'scheduler.delete_workload'
    success_message = "Card deleted successfully"

    def delete(self, request, *args, **kwargs):
        """
        Display success message
        Adapted from: https://stackoverflow.com/questions/24822509/
        success-message-in-deleteview-not-shown
        """
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(DeleteWorkload, self).delete(request, *args, **kwargs)


class AllDeleteWorkload(
        LoginRequiredMixin,
        PermissionRequiredMixin,
        DeleteView
            ):
    """
    Displays the page to confirm deletion of a workload card
    """
    model = Workload
    template_name = 'all_delete_workload.html'
    success_url = '/all_scheduler'
    permission_required = 'scheduler.delete_workload'
    success_message = "Card deleted successfully"

    def delete(self, request, *args, **kwargs):
        """
        Display success message
        Adapted from: https://stackoverflow.com/questions/24822509/
        success-message-in-deleteview-not-shown
        """
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(AllDeleteWorkload, self).delete(request, *args, **kwargs)


class ToggleWorkload(
        LoginRequiredMixin,
        PermissionRequiredMixin,
        View
            ):
    """
    Toggles the status of a workload card
    """
    permission_required = 'scheduler.change_workload'

    def post(self, request, pk, *args, **kwargs):
        toggle_workload = get_object_or_404(Workload, pk=pk)
        if toggle_workload.status == "To Do":
            toggle_workload.status = "Completed"
            messages.success(self.request, "Card completed successfully")
        toggle_workload.save()
        return redirect('scheduler')


class AllToggleWorkload(
        LoginRequiredMixin,
        PermissionRequiredMixin,
        View
            ):
    """
    Toggles the status of a workload card
    """
    permission_required = 'scheduler.change_workload'

    def post(self, request, pk, *args, **kwargs):
        toggle_workload = get_object_or_404(Workload, pk=pk)
        if toggle_workload.status == "To Do":
            toggle_workload.status = "Completed"
            messages.success(self.request,
                             "Card status changed to Completed successfully")
        else:
            toggle_workload.status = "To Do"
            messages.success(self.request,
                             "Card status changed to To Do successfully")
        toggle_workload.save()
        return redirect('all_scheduler')


# Analysts Page


class AnalystList(
        LoginRequiredMixin,
        PermissionRequiredMixin,
        generic.ListView
        ):
    """
    Displays a list of all analysts
    """
    model = Analyst
    queryset = Analyst.objects.order_by('status', 'name')
    template_name = 'analysts.html'
    paginate_by = 15
    permission_required = 'scheduler.view_analyst'


class AddAnalyst(
        LoginRequiredMixin,
        PermissionRequiredMixin,
        SuccessMessageMixin,
        CreateView
            ):
    """
    Displays the page to add a new analyst to the list
    """
    model = Analyst
    fields = ['work_id', 'name', 'status']
    template_name = 'add_analyst.html'
    success_url = '/analysts'
    permission_required = 'scheduler.add_analyst'
    success_message = "%(name)s added successfully"


class UpdateAnalyst(
        LoginRequiredMixin,
        PermissionRequiredMixin,
        SuccessMessageMixin,
        UpdateView
            ):
    """
    Displays the page to update an analyst
    """
    model = Analyst
    fields = ['name', 'status']
    template_name = 'update_analyst.html'
    success_url = '/analysts'
    permission_required = 'scheduler.change_analyst'
    success_message = "%(name)s updated successfully"


class DeleteAnalyst(
        LoginRequiredMixin,
        PermissionRequiredMixin,
        DeleteView
            ):
    """
    Displays the page to confirm deletion of an analyst
    """
    model = Analyst
    template_name = 'delete_analyst.html'
    success_url = '/analysts'
    permission_required = 'scheduler.delete_analyst'
    success_message = "%(name)s deleted successfully"

    def delete(self, request, *args, **kwargs):
        """
        Display success message
        Adapted from: https://stackoverflow.com/questions/24822509/
        success-message-in-deleteview-not-shown
        """
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(DeleteAnalyst, self).delete(request, *args, **kwargs)


class ToggleAnalyst(
        LoginRequiredMixin,
        PermissionRequiredMixin,
        View
            ):
    """
    Toggles the status of an analyst
    """
    permission_required = 'scheduler.change_analyst'

    def post(self, request, pk, *args, **kwargs):
        toggle_analyst = get_object_or_404(Analyst, pk=pk)
        if toggle_analyst.status == "Active":
            toggle_analyst.status = "Inactive"
            messages.success(self.request,
                             "Analyst status changed to Inactive successfully")
        else:
            toggle_analyst.status = "Active"
            messages.success(self.request,
                             "Analyst status changed to Active successfully")
        toggle_analyst.save()
        return redirect('analysts')


# Tests Page

class TestList(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    generic.ListView
        ):
    """
    Displays a list of all tests
    """
    model = Test
    queryset = Test.objects.order_by('status', 'name')
    template_name = 'tests.html'
    paginate_by = 15
    permission_required = 'scheduler.view_test'


class AddTest(
        LoginRequiredMixin,
        PermissionRequiredMixin,
        SuccessMessageMixin,
        CreateView
            ):
    """
    Displays the page to add a new test to the list
    """
    model = Test
    fields = ['name', 'status']
    template_name = 'add_test.html'
    success_url = '/tests'
    permission_required = 'scheduler.add_test'
    success_message = "%(name)s added successfully"


class UpdateTest(
        LoginRequiredMixin,
        PermissionRequiredMixin,
        SuccessMessageMixin,
        UpdateView
            ):
    """
    Displays the page to update an test
    """
    model = Test
    fields = ['name', 'status']
    template_name = 'update_test.html'
    success_url = '/tests'
    permission_required = 'scheduler.change_test'
    success_message = "%(name)s updated successfully"


class DeleteTest(
        LoginRequiredMixin,
        PermissionRequiredMixin,
        DeleteView
            ):
    """
    Displays the page to confirm deletion of an test
    """
    model = Test
    template_name = 'delete_test.html'
    success_url = '/tests'
    permission_required = 'scheduler.delete_test'
    success_message = "%(name)s deleted successfully"

    def delete(self, request, *args, **kwargs):
        """
        Display success message
        Adapted from: https://stackoverflow.com/questions/24822509/
        success-message-in-deleteview-not-shown
        """
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(DeleteTest, self).delete(request, *args, **kwargs)


class ToggleTest(
        LoginRequiredMixin,
        PermissionRequiredMixin,
        View):
    """
    Toggles the status of a test
    """
    permission_required = 'scheduler.change_test'

    def post(self, request, pk, *args, **kwargs):
        toggle_test = get_object_or_404(Test, pk=pk)
        if toggle_test.status == "Active":
            toggle_test.status = "Inactive"
            messages.success(self.request,
                             "Test status changed to Inactive successfully")
        else:
            toggle_test.status = "Active"
            messages.success(self.request,
                             "Test status changed to Active successfully")
        toggle_test.save()
        return redirect('tests')
