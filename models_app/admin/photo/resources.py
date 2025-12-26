from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html

from models_app.models import Photo


@admin.action(description="Одобрить выбранные фотографии")
def make_approved(modeladmin, request, queryset):
    queryset.update(state="approved", publication_date=timezone.now())

@admin.action(description="Отклонить выбранные фотографии")
def make_rejected(modeladmin, request, queryset):
    queryset.update(state="rejected")


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    date_hierarchy = "publication_date"
    fields = [
        ("author", "title"),
        "image_preview",
        "state",
        "publication_date",
        "description",
    ]

    exclude = ["image"]
    readonly_fields = ["image_preview", "author"]

    list_display = ["title", "state", "publication_date"]
    list_filter = ["state", "author"]

    actions = [make_approved, make_rejected]

    @admin.display(description="Фото")
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-width:100%; max-height:600px;" />',
                obj.image.url,
            )
