from django.contrib import admin

from posts.models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["user", "created_at", "caption"]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["user", "created_at", "text"]