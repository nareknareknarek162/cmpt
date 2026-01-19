from django.contrib import admin

from models_app.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ["photo", "author"]

    list_filter = []
    list_display = ["text", "author", "created_at"]
