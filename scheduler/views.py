from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic, View
from django.views.generic import CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import WorkloadForm
from .models import Workload, Analyst, Test
from .filters import WorkloadFilter, AllWorkloadFilter


# Scheduler Page


class WorkloadList(LoginRequiredMixin, generic.ListView):
    """
    Displays the workload cards that have a status of To Do
    """
    model = Workload
    filterset_class = WorkloadFilter
    template_name = 'scheduler.html'
    paginate_by = 12

    def get_context_data(self, **kwargs):
        """ tracker table search filters """
        context = super().get_context_data(**kwargs)
        context['filter'] = WorkloadFilter(self.request.GET,
                                           queryset=Workload.objects.order_by(
                                            'test_date'), )
        return context


class AllWorkloadList(LoginRequiredMixin, generic.ListView):
    """
    Displays all workload cards
    """
    model = Workload
    template_name = 'all_scheduler.html'
    paginate_by = 12

    def get_context_data(self, **kwargs):
        """ tracker table search filters """
        context = super().get_context_data(**kwargs)
        context['filter'] = AllWorkloadFilter(self.request.GET,
                                           queryset=Workload.objects.order_by(
                                            'test_date'), )
        return context

class AddWorkload(LoginRequiredMixin, CreateView):
    """
    Displays the page to add a new workload card
    """
    model = Workload
    form_class = WorkloadForm
    template_name = 'add_workload.html'
    success_url = '/scheduler'


class UpdateWorkload(LoginRequiredMixin, UpdateView):
    """
    Displays the page to update a workload card
    """
    model = Workload
    form_class = WorkloadForm
    template_name = 'update_workload.html'
    success_url = '/scheduler'


class DeleteWorkload(LoginRequiredMixin, DeleteView):
    """
    Displays the page to confirm deletion of a workload card
    """
    model = Workload
    template_name = 'delete_workload.html'
    success_url = '/scheduler'


class AllDeleteWorkload(LoginRequiredMixin, DeleteView):
    """
    Displays the page to confirm deletion of a workload card
    """
    model = Workload
    template_name = 'all_delete_workload.html'
    success_url = '/all_scheduler'


class ToggleWorkload(LoginRequiredMixin, View):
    """
    Toggles the status of a workload card
    """
    def post(self, request, pk, *args, **kwargs):
        toggle_workload = get_object_or_404(Workload, pk=pk)
        if toggle_workload.status == "To Do":
            toggle_workload.status = "Completed"
        else:
            toggle_workload.status = "To Do"
        toggle_workload.save()
        return redirect('scheduler')


class AllToggleWorkload(LoginRequiredMixin, View):
    """
    Toggles the status of a workload card
    """
    def post(self, request, pk, *args, **kwargs):
        toggle_workload = get_object_or_404(Workload, pk=pk)
        if toggle_workload.status == "To Do":
            toggle_workload.status = "Completed"
        else:
            toggle_workload.status = "To Do"
        toggle_workload.save()
        return redirect('all_scheduler')


# Analysts Page


class AnalystList(LoginRequiredMixin, generic.ListView):
    """
    Displays a list of all analysts
    """
    model = Analyst
    queryset = Analyst.objects.order_by('status', 'name')
    template_name = 'analysts.html'
    paginate_by = 15


class AddAnalyst(LoginRequiredMixin, CreateView):
    """
    Displays the page to add a new analyst to the list
    """
    model = Analyst
    fields = ['name', 'status']
    template_name = 'add_analyst.html'
    success_url = '/analysts'


class UpdateAnalyst(LoginRequiredMixin, UpdateView):
    """
    Displays the page to update an analyst
    """
    model = Analyst
    fields = ['name', 'status']
    template_name = 'update_analyst.html'
    success_url = '/analysts'


class DeleteAnalyst(LoginRequiredMixin, DeleteView):
    """
    Displays the page to confirm deletion of an analyst
    """
    model = Analyst
    template_name = 'delete_analyst.html'
    success_url = '/analysts'


class ToggleAnalyst(LoginRequiredMixin, View):
    """
    Toggles the status of an analyst
    """
    def post(self, request, pk, *args, **kwargs):
        toggle_analyst = get_object_or_404(Analyst, pk=pk)
        if toggle_analyst.status == "Active":
            toggle_analyst.status = "Inactive"
        else:
            toggle_analyst.status = "Active"
        toggle_analyst.save()
        return redirect('analysts')


# Tests Page

class TestList(LoginRequiredMixin, generic.ListView):
    """
    Displays a list of all tests
    """
    model = Test
    queryset = Test.objects.order_by('status', 'name')
    template_name = 'tests.html'
    paginate_by = 15


class AddTest(LoginRequiredMixin, CreateView):
    """
    Displays the page to add a new test to the list
    """
    model = Test
    fields = ['name', 'status']
    template_name = 'add_test.html'
    success_url = '/tests'


class UpdateTest(LoginRequiredMixin, UpdateView):
    """
    Displays the page to update an test
    """
    model = Test
    fields = ['name', 'status']
    template_name = 'update_test.html'
    success_url = '/tests'


class DeleteTest(LoginRequiredMixin, DeleteView):
    """
    Displays the page to confirm deletion of an test
    """
    model = Test
    template_name = 'delete_test.html'
    success_url = '/tests'


class ToggleTest(LoginRequiredMixin, View):
    """
    Toggles the status of a test
    """
    def post(self, request, pk, *args, **kwargs):
        toggle_test = get_object_or_404(Test, pk=pk)
        if toggle_test.status == "Active":
            toggle_test.status = "Inactive"
        else:
            toggle_test.status = "Active"
        toggle_test.save()
        return redirect('tests')
