from django.db import models
from django.db.models.fields import CharField, TextField, URLField
from django.db.models.fields.files import ImageField


class Project(models.Model):
    title = CharField(max_length=100)
    description = TextField()
    image = ImageField(upload_to='portfolio/images/')
    url = URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
