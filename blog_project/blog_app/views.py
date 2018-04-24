from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models, forms
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

class About_View(TemplateView):

    template_name = 'about.html'


class Post_List_View(ListView):

    model = models.Post

    def get_queryset(self):
        return models.Post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')


class Post_Detail_View(DetailView):

    model = models.Post


@login_required
def add_comment_to_post(request, pk):

    post = get_object_or_404(models.Post, pk=pk)

    if request.method == 'POST':
        form = forms.Comment_Form(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)

    else:
        form = forms.Comment_Form()

    return render(request, 'blog_app/comment_form.html', context={'form':form})



@login_required
def post_publish(request, pk):
    post = get_object_or_404(models.Post, pk=pk)
    # print("I'm publishing")
    post.publish()
    return redirect('post_detail', pk=post.pk)



@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(models.Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)



@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(models.Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)




class Post_Create_View(CreateView, LoginRequiredMixin):

    login_url = '/login/'

    redirect_field_name = 'blog_app/post_detail.html'

    form_class = forms.Post_Form

    model = models.Post



class Post_Update_View(LoginRequiredMixin, UpdateView):

    login_url = '/login/'

    redirect_field_name = 'blog_app/post_detail.html'

    form_class = forms.Post_Form

    model = models.Post



class Post_Delete_View(DeleteView, LoginRequiredMixin):
    
    success_url = reverse_lazy('posts_list')

    model = models.Post



class Draft_List_View(ListView, LoginRequiredMixin):

    login_url = '/login/'

    redirect_field_name = 'blog_app/post_detail.html' 

    model = models.Post

    def get_queryset(self):
        return models.Post.objects.filter(publish_date__isnull=True).order_by('-create_date')
