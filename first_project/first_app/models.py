from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.name


class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    
    def get_absolute_url(self):
        return reverse("first_app:school_detail", kwargs={'pk':self.pk})

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, related_name='students', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class WebPage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    webpage = models.ForeignKey(WebPage, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.date)


# Do not create your own User model but add additional
# attributes to the built-in python's User model
class UserProfileInfo(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # additional attributes
    portfolio_site = models.URLField(blank=True)
    profile_picture = models.ImageField(upload_to='../media/images/profile_pics', blank=True)

    def __str__(self):
        return self.user.username


