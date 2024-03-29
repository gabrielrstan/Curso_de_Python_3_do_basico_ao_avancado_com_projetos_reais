from blog.views import index, post, page
from django.urls import path  # type:ignore


app_name = 'blog'
urlpatterns = [
    path('', index, name='index'),
    path('post/', post, name='post'),
    path('page/', page, name='page'),
]
