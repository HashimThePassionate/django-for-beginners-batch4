from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView, BlogAnauthorizedView

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    path('<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('unauthorized/', BlogAnauthorizedView.as_view(), name='au'),

]
