from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic, View
from django.views.generic import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from .models import Analyst, Test, Workload


# Analysts Page

class AnalystList(LoginRequiredMixin, generic.ListView):
    """
    Displays a list of all analysts
    """
    model = Analyst
    queryset = Analyst.objects.order_by('status', 'name')
    template_name = 'analysts.html'
    paginate_by = 20


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
    Displays the page to confrirm deletion of an analyst
    """
    model = Analyst
    template_name = 'delete_analyst.html'
    success_url = '/analysts'


# Tests Page

class TestList(LoginRequiredMixin, generic.ListView):
    """
    Displays a list of all tests
    """
    model = Test
    queryset = Test.objects.order_by('status', 'name')
    template_name = 'tests.html'
    paginate_by = 20


class AddTest(LoginRequiredMixin, CreateView):
    """
    Displays the page to add a new test to the list
    """
    model = Test
    fields = ['name', 'status']
    template_name = 'add_test.html'
    success_url = '/tests'
