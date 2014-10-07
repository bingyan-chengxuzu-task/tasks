from blog.models import Tag, Author, Article, Classification
from django.contrib import admin
            
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'website')
    search_fields = ('name',)
            
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('caption', 'subcaption', 'classification', 'author', 'publish_time', 'update_time')
    list_filter = ('publish_time',)
    date_hierarchy = 'publish_time'
    ordering = ('-publish_time',)
    filter_horizontal = ('tags',)
            
admin.site.register(Article, ArticleAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag)
admin.site.register(Classification)