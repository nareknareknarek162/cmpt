from django.contrib import admin

from models_app.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name"]

    search_fields = ["username", "first_name", "last_name"]
    exclude = ["password"]
    readonly_fields = [
        field.name
        for field in User._meta.fields
        if field.name not in ("password", "is_superuser", "is_staff")
    ]
