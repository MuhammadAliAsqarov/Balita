from django.contrib import admin
from .models import Category, Post, Comment, Contact, Tag
from django.utils.html import format_html
from datetime import datetime


class PostInline(admin.TabularInline):
    model = Post
    extra = 0
    fields = ('title', 'is_published')


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    list_display_links = ('id', 'name')

    inlines = (PostInline,)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','post_count')
    list_display_links = ('id', 'name')

    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = 'Number of Posts'
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',  'created_at', 'views', 'is_published')
    list_display_links = ('id', 'title')

    inlines = (CommentInline,)

    search_fields = ['title']
    list_filter = ['is_published']

    def preview_image(self, obj):
        return format_html("<img height=70 src={}>", obj.image.url)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    list_display_links = ('name', 'email')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'solved', 'days', 'created_at')
    list_display_links = ('id', 'name')

    def days(self, obj):
        days_diff = (datetime.now() - obj.created_at).days
        if days_diff > 3:
            color = 'red'
        else:
            color = 'purple'
        if obj.solved:
            color = 'green'
        return format_html("<div style='color: {}'>{}</div>", color, days_diff)
