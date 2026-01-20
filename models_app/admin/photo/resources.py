from django.contrib import admin, messages
from django.utils import timezone
from django.utils.html import format_html
from viewflow.fsm import TransitionNotAllowed

from models_app.models import Photo


@admin.action(description="Одобрить выбранные фотографии")
def make_approved(modeladmin, request, queryset):
    for photo in queryset:
        try:
            photo.flow.approve()
            photo.publication_date = timezone.now()
            photo.save()
        except TransitionNotAllowed:
            messages.warning(request, "Выбранные фотографии нельзя одобрить")


@admin.action(description="Отклонить выбранные фотографии")
def make_rejected(modeladmin, request, queryset):
    for photo in queryset:
        try:
            photo.flow.reject()
            photo.save()
        except TransitionNotAllowed:
            messages.warning(request, "Выбранные фотографии нельзя отклонить")


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
    # change_form_template =

    list_display = ["title", "state", "publication_date", "author"]
    list_filter = ["state"]
    search_fields = ["title", "author", "publication_date"]

    actions = [make_approved, make_rejected]

    @admin.display(description="Фото")
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-width:100%; max-height:600px;" />',
                obj.image.url,
            )
