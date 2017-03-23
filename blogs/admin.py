from django.contrib import admin
from .models import Author, Article
from .forms import ArticleModelAdminForm


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_published',)
    form = ArticleModelAdminForm


admin.site.register(Article, ArticleAdmin)
admin.site.register(Author)
