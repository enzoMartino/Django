from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models, forms
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

class About_View(TemplateView):

    template_name = 'about.html'


class Post_List_View(ListView):

    model = models.Post

    def get_queryset(self):
        return models.Post.objects.filter(publish_date__lte=timezone.now()).order_by('-published_date')


class Post_Detail_View(DetailView):

    model = models.Post



class Post_Create_View(CreateView, LoginRequiredMixin):

    login_url = '/login/'

    redirect_field_name = 'blog/post_detail.html'

    form_class = forms.Post_Form

    model = models.Post



class Post_Update_View(LoginRequiredMixin, UpdateView):

    login_url = '/login/'

    redirect_field_name = 'blog/post_detail.html'

    form_class = forms.Post_Form

    model = models.Post



class Post_Delete_View(DeleteView, LoginRequiredMixin):
    
    success_url = reverse_lazy('post_list')

    model = models.Post



class Draft_List_View(ListView, LoginRequiredMixin):

    login_url = '/login/'

    redirect_field_name = 'blog/post_detail.html' 

    model = models.Post

    def get_queryset(self):
        return models.Post.objects.filter(publish_date__isnull=True).order_by('-create_date')
