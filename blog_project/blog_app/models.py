from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Post(models.Model):

    # ATTRIBUTES
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateField(default=timezone.now)
    publish_date = models.DateField(blank=True, null=True)

    # METHODS
    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(is_approved=True)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.title



class Comment(models.Model):

    # ATTRIBUTES
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateField(default=timezone.now)
    is_approved = models.BooleanField(default=False)

    # METHODS
    def approve(self):
        self.is_approved = True
        self.save()

    def get_absolute_url(self):
        return reverse('posts_list')

    def __str__(self):
        return self.text