from django.contrib import admin
from django.utils.html import format_html

from models_app.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ["photo", "author"]

    list_display = ["text", "author_link", "created_at"]
    search_fields = ["text", "author__username", "created_at"]

    def author_link(self, obj):
        return format_html(
            '<a href="/admin/models_app/user/{}/change/">{}</a>',
            obj.author.pk,
            obj.author.username,
        )
