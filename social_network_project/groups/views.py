from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse
from django.views import generic
from . import models

# Create your views here.

class CreateGroup(LoginRequiredMixin, generic.CreateView):

    fields = ('name', 'description')

    model = models.Group


class SingleGroup(generic.DeleteView):

    model = models.Group


class ListGroups(generic.ListView):

    model = models.Group
