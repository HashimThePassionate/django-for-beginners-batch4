from django.urls import path
from .views import post_list, PostList
urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/', PostList.as_view(), name='postlist'),
]
