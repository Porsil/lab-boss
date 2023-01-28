from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic, View
from django.views.generic import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from .models import Workload, Analyst, Test


# Scheduler Page


class WorkloadList(LoginRequiredMixin, generic.ListView):
    """
    Displays the workload cards that have a status of To Do
    """
    model = Workload()
    queryset = Workload.objects.filter(status='To Do').order_by(
        'test_date', 'analyst')
    template_name = 'scheduler.html'
    paginate_by = 10


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
