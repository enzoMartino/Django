from django.urls import path
from first_app import views

app_name = 'first_app'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('help/', views.help, name = 'help'),
    path('image/', views.image, name = 'image'),
    path('users/', views.users, name = 'users'),
    path('access_records/', views.access_records, name = 'access_records'),
    path('sign_up/', views.sign_up, name = 'sign_up'),
    path('sign_in/', views.sign_in, name = 'sign_in'),
]