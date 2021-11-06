import datetime

from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/images/')
    date = models.DateField(datetime.date.today())
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
