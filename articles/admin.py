from django.contrib import admin
from .models import Article, Category

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'category', 'slug')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    # Creates lookup widget for author, rather than dropdown menu
    # raw_id_fields = ('author',)

admin.site.register(Article, ArticleAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Category, CategoryAdmin)
