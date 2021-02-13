from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.get_posts, name='posts'),
    path('posts/<int:post_id>/', views.get_posts, name='post')
]
