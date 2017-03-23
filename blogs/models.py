from __future__ import unicode_literals
from tinymce import models as tinymce_models

from django.db import models

class Author(models.Model):
    pro_pic = models.ImageField()
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    hometown = models.CharField(max_length=20)
    university = models.CharField(max_length=50)
    bio = models.TextField()

class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    date_published = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete= models.CASCADE)
    pic = models.URLField()
    content = tinymce_models.HTMLField()
