from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns=[
    path('create/', views.create_blog_view, name='create'),
]