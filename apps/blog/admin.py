from django.contrib import admin
from .models import Post
# Register your models here.

admin.site.site_header = "Blog Admin"
admin.site.site_title = "Blog Admin Portal"
admin.site.index_title = "Welcome to Blog Admin Portal"
admin.site.register(Post)