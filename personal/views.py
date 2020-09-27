from operator import attrgetter
from django.shortcuts import render
# from account.models import *
from blog.models import *
from blog.views import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
BLOG_POSTS_PER_PAGE = 10


def home_screen_view(request):
    context = {}

    # Search
    query = ""
    if request.GET:
        query = request.GET.get('q', '')
        context['query'] = str(query)

    blog_posts = sorted(get_blog_queryset(query), key=attrgetter('date_updated'), reverse=True)

    # Pagination
    page = request.GET.get('page', 1)
    blog_posts_paginator = Paginator(blog_posts, BLOG_POSTS_PER_PAGE)
    try:
        blog_posts = blog_posts_paginator.page(page)
    except PageNotAnInteger:
        blog_posts = blog_posts_paginator.page(BLOG_POSTS_PER_PAGE)
    except EmptyPage:
        blog_posts = blog_posts_paginator.page(blog_posts_paginator.num_pages)

    context['blog_posts'] = blog_posts

    return render(request, "personal/home.html", context)
