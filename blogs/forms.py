from django.forms import ModelForm
from django import forms
from .widgets import AdvancedEditor
from .models import Article
from django.db import models
from django.forms import inlineformset_factory
from .models import Article,Author


class ArticleModelAdminForm(ModelForm):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=AdvancedEditor())
    description = forms.CharField(max_length=300)
    AuthorFormSet = inlineformset_factory(Author,Article, fields=['author',])
    pic = forms.ImageField()

    class Meta:
        model = Article
        fields = ['title','content','description','author','pic','category']

