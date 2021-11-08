from django.urls import path
from .views import render_posts, post_by_id

app_name = 'blog'
urlpatterns = [
    path('', render_posts, name='posts'),
    path('post/<int:post_id>', post_by_id, name='posts_by_id'),
]
