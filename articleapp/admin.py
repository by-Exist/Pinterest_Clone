from articleapp.models import Article
from django.contrib import admin

# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass