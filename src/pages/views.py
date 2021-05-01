from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def home_view(request, *args, **kwargs):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'home.html', context)
# Create your views here.

def about_view(request, *args, **kwargs):
    return render(request, 'about.html', {})