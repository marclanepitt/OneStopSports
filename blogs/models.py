from __future__ import unicode_literals
from tinymce import models as tinymce_models
from django_extensions.db import fields
from django.db import models
import secretballot
from oss.settings import MEDIA_ROOT

class Author(models.Model):
    pro_pic = models.ImageField(upload_to= MEDIA_ROOT)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    hometown = models.CharField(max_length=20)
    university = models.CharField(max_length=50)
    bio = models.TextField()

    def __unicode__(self):
        return self.first_name

class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    date_published = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete= models.CASCADE)
    pic = models.ImageField(upload_to=MEDIA_ROOT)
    content = tinymce_models.HTMLField()
    HOCKEY = 'Hockey'
    SOCCER = 'Soccer'
    BASKETBALL = 'Basketball'
    BASEBALL = 'Baseball'
    FOOTBALL = 'Football'
    COLLEGE_HOCKEY = 'College Hockey'
    COLLEGE_SOCCER = 'College Soccer'
    COLLEGE_BASKETBALL = 'College Basketball'
    COLLEGE_BASEBALL = 'College Baseball'
    COLLEGE_FOOTBALL = 'College Football'
    OTHER = 'other'

    SPORTS = (
        (HOCKEY,'Hockey'),
        (SOCCER , 'Soccer'),
        (BASKETBALL , 'Basketball'),
        (BASEBALL , 'Baseball'),
        (FOOTBALL , 'Football'),
        (COLLEGE_HOCKEY , 'College Hockey'),
        (COLLEGE_SOCCER , 'College Soccer'),
        (COLLEGE_BASKETBALL , 'College Basketball'),
        (COLLEGE_BASEBALL , 'College Baseball'),
        (COLLEGE_FOOTBALL , 'College Football'),
        (OTHER , 'other'),
    )
    category = models.CharField(max_length=30,choices=SPORTS,default=OTHER)
    slug = fields.AutoSlugField(populate_from='title')

    def __unicode__(self):
        return self.title


secretballot.enable_voting_on(Article)
