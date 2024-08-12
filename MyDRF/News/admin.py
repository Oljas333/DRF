from django.contrib import admin
from .models import ArtiLes, Category, Comment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')

class ComentInLine(admin.StackedInline):
    model = Comment
    fields = ('author', 'text', 'article')
    extra = 1

@admin.register(ArtiLes)
class ArtiLesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'date')
    list_filter = ('category', 'date')
    search_fields = ('title', 'anons', 'full_text')
    list_editable = ('title', 'category', 'date')
    list_per_page = 10
    list_max_show_all = 100
    inlines = [ComentInLine,]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'text', 'article')
    list_filter = ('author', 'created_at')
    search_fields = ('author',)