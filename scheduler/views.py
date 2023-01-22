from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic, View
from django.views.generic import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from .models import Analyst, Test, Workload


class AnalystList(LoginRequiredMixin, generic.ListView):
    model = Analyst
    queryset = Analyst.objects.order_by('status', 'name')
    template_name = 'analysts.html'
    paginate_by = 20


class AddAnalyst(LoginRequiredMixin, CreateView):
    model = Analyst
    fields = ['name', 'status']
    template_name = 'add_analyst.html'
    success_url = '/analysts'
