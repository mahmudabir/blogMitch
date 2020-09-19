from django.shortcuts import render, redirect

from account.models import *
from blog.models import *
from blog.forms import *


# Create your views here.
def create_blog_view(request):
    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')

    form = CreateBlogPostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        author = Account.objects.filter(email=request.user.email).first()
        obj.author = author
        obj.save()
        form = CreateBlogPostForm()

    context['form'] = form

    return render(request, 'blog/create_blog.html', context)
