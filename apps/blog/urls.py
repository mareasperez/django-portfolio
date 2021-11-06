from django.urls import path
from .views import posts

app_name = 'posts'
urlpatterns = [
    path('',  posts, name='posts'),
]
