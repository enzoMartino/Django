from django.urls import path
from first_app import views

app_name = 'first_app'

urlpatterns = [
    path('help/', views.help, name = 'help'),
    path('image/', views.image, name = 'image'),
    path('users/', views.users, name = 'users'),
    path('access_records/', views.access_records, name = 'access_records'),
    path('sign_up/', views.sign_up, name = 'sign_up'),
    path('sign_in/', views.sign_in, name = 'sign_in'),
    path('school_detail/<int:pk>/', views.School_Detail_View.as_view(), name = 'school_detail'),
    path('school_list/', views.School_List_View.as_view(), name = 'school_list'),
    path('school_create/', views.School_Create_View.as_view(), name = 'school_create'),
    path('school_update/<int:pk>/', views.School_Update_View.as_view(), name = 'school_update'),
    path('school_delete/<int:pk>/', views.School_Delete_View.as_view(), name = 'school_delete'),
]