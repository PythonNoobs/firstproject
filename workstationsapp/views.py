from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Workstation
from django.urls import reverse_lazy


class ListWorkstations(ListView):
    model = Workstation
    template_name = 'workstationsapp/list_workstations.html'


class AddWorkstation(CreateView):
    model = Workstation
    fields = [
        'title', 'model'
    ]
    template_name = 'workstationsapp/add_workstation.html'
    success_url = reverse_lazy('workstationsapp:list_workstations')


class EditWorkstation(UpdateView):
    model = Workstation
    fields = [
        'title', 'model'
    ]
    template_name = 'workstationsapp/edit_workstation.html'
    success_url = reverse_lazy('workstationsapp:list_workstations')


class DeleteWorkstation(DeleteView):
    model = Workstation
    success_url = reverse_lazy('workstationsapp:list_workstations')