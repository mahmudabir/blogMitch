from django.shortcuts import render
from blog.models import *
# Create your views here.
def create_blog_view(request):
    context = {}
    return render(request, 'blog/create_blog.html', context)