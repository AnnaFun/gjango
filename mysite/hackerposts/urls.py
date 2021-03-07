from django.urls import path, include
from hackerposts import views

urlpatterns = [
    path('posts/', views.post_list, name='posts'),
    path('posts/<int:post_id>/', views.PostDetaiView.as_view(), name='post'),
    path('posts/create', views.PostCreateView.as_view(), name='create_post'),
    path('posts/<int:post_pk/add_comm', views.add_comm, name='comment')

    # path('posts/', views.PostList.as_view(), name='posts'),
    # path('posts/<int:pk>', views.PostDetail.as_view(), name='post')



    #    path('posts/create', views.CreateView.as_view, name='create_post')
]
