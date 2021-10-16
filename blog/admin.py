from django.contrib import admin
from blog.models import Post, Tag, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "text",
        "slug",
        "image",
        "author",
        "published_at",
    )
    list_editable = (
        # "title",
        "text",
        "slug",
        "image",
        "author",
    )
    raw_id_fields = (
        "author",
        "likes",
    )


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "post",
        "text",
        "author",
        "published_at",
    )
    list_editable = ("text",)
    raw_id_fields = (
        "author",
        "post",
    )


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
