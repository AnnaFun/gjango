from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def get_posts(request):
    posts = Post.objects.all()

    context = {
        'posts': posts
    }


    return render(request, 'posts.html', context=context)
#    text = ''
#    for post in posts:
#       text += f'text' \
#                f': {post.text} an: {post.author_name} date: {post.pub_date}<br>'
#        return HttpResponse(text)