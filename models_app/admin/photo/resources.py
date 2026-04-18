from django.contrib import admin, messages
from django.utils import timezone
from django.utils.html import format_html
from viewflow.fsm import TransitionNotAllowed

from models_app.models import Photo
from models_app.models.photo.fsm import State


@admin.action(description="Одобрить выбранные фотографии")
def make_approved(modeladmin, request, queryset):
    for photo in queryset:
        try:
            photo.flow.approve()
            photo.publication_date = timezone.now()
            photo.save()
        except TransitionNotAllowed:
            messages.warning(request, f"Фотографию {photo} нельзя одобрить")


@admin.action(description="Отклонить выбранные фотографии")
def make_rejected(modeladmin, request, queryset):
    for photo in queryset:
        try:
            photo.flow.reject()
            photo.save()
        except TransitionNotAllowed:
            messages.warning(request, f"Фотографию {photo} нельзя отклонить")


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    date_hierarchy = "publication_date"
    fields = [
        ("author", "title"),
        "image_preview",
        "previous_image_preview",
        "state",
        "publication_date",
        "description",
    ]

    exclude = ["image"]
    readonly_fields = [
        "image_preview",
        "previous_image_preview",
        "publication_date",
        "author",
        "title",
        "description",
    ]

    list_display = ["title", "state", "publication_date", "author"]
    list_filter = ["state"]
    search_fields = ["title", "author__username", "publication_date"]

    actions = [make_approved, make_rejected]

    @admin.display(description="Текущее фото")
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-width:100%; max-height:600px;" />',
                obj.image.url,
            )

    @admin.display(description="Предыдущее фото")
    def previous_image_preview(self, obj):
        if obj.previous_image:
            return format_html(
                '<img src="{}" style="max-width:100%; max-height:600px; opacity: 0.5;" />',
                obj.previous_image.url,
            )

    def formfield_for_choice_field(self, db_field, request, **kwargs):
        if db_field.name == "state":
            id = request.resolver_match.kwargs.get("object_id")
            if not id:
                return super().formfield_for_choice_field(db_field, request, **kwargs)

            try:
                pic = Photo.objects.get(pk=id)
            except Photo.DoesNotExist:
                return super().formfield_for_choice_field(db_field, request, **kwargs)

            if pic.state == State.ON_MODERATION:
                kwargs["choices"] = [
                    (State.APPROVED, "Approved"),
                    (State.REJECTED, "Rejected"),
                ]
            elif pic.state == State.APPROVED:
                kwargs["choices"] = [
                    (State.REJECTED, "Rejected"),
                    (State.ON_MODERATION, "On Moderation"),
                ]
            return super().formfield_for_choice_field(db_field, request, **kwargs)

    def has_add_permission(self, request):
        return False
