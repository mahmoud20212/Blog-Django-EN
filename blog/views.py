from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
posts = [
    {
        'author': 'Mahmoud',
        'title': 'Blog Post 1',
        'content': 'Hello World',
        'date_posted': 'August 28, 2018',
    },
    {
        'author': 'Mahmoud',
        'title': 'Blog Post 1',
        'content': 'Mahmoud',
        'date_posted': 'August 28, 2022',
    },
]


def index(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/index.html', context)

def about(request):
    context = {
        'title': 'About'
    }
    return HttpResponse('<h1>Blog about</h1>')