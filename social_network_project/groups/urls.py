from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'groups'

urlpatterns = [
   path('', views.ListGroups.as_view(), 'all'),
   path('new/', views.CreateGroup.as_view(), name = 'create'),
   path('posts/in/<slug:slug>/', views.SingleGroup.as_view(), name = 'single'),
   
]