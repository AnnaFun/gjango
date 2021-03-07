from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseGone
from django.views.generic import CreateView, DetailView

from .forms import PostForm
from .models import Post


# class PostListView(ListView):
#     template_name = 'posts.html'
#     context_object_name = 'posts'

def post_list(request):

    posts = Post.objects.order_by('-pub_date')

    p = Paginator(posts, 5)

    page_number = request.GET.get('page', 1)

    context = {
        'posts': p.page(page_number)
    }
    return render(request, 'posts.html', context=context)


class PostDetaiView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'post.html'


class PostCreateView(CreateView):
    model = Post
    fields = ('author_name', 'text')
    template_name = 'post_form.html'


def add_comm(request, post_pk):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post', post_pk)


