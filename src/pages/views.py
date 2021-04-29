from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]


def home_view(request, *args, **kwargs):
    context = {
        'posts': posts
    }
    return render(request, 'home.html', context)
# Create your views here.

def about_view(request, *args, **kwargs):
    return render(request, 'about.html', {})