from django.contrib import admin, messages
from django.shortcuts import render
from django.urls import path

from models_app.models import User
from notifications.services import broadcast_message


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    change_list_template = "admin/users_changelist.html"

    def get_urls(self):
        urls = super().get_urls()

        custom_urls = [
            path(
                "broadcast/",
                self.admin_site.admin_view(self.broadcast_view),
                name="users_broadcast",
            ),
        ]

        return custom_urls + urls

    def broadcast_view(self, request):
        if request.method == "POST":
            message = request.POST.get("message", "").strip()
            if message:
                broadcast_message(message)
                messages.success(request, "Глобальное уведомление успешно отправлено!")
            else:
                messages.error(request, "Текст сообщения не может быть пустым.")
        return render(request, "admin/broadcast_message_page.html")

    list_display = ["username", "first_name", "last_name"]

    search_fields = ["username", "first_name", "last_name"]
    exclude = ["password"]
    readonly_fields = [
        field.name
        for field in User._meta.fields
        if field.name not in ("password", "is_superuser", "is_staff")
    ]
