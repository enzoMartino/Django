from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.About_View.as_view(), name = 'about'),
    path('', views.Post_List_View.as_view(), name = 'posts_list'),
    path('post/<int:pk>', views.Post_Detail_View.as_view(), name = 'post_detail'),
    path('post/create/', views.Post_Create_View.as_view(), name = 'post_create'),
    path('post/<int:pk>/update/', views.Post_Update_View.as_view(), name = 'post_update'),
    path('post/<int:pk>/delete/', views.Post_Delete_View.as_view(), name = 'post_delete'),
    path('drafts_list/', views.Draft_List_View.as_view(), name = 'drafts_list'),
]
