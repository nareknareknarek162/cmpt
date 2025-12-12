from django.views.generic import ListView

from models_app.models import Photo


class AccountView(ListView):
    model = Photo
    # paginate_by = 6
    template_name = "account.html"
    context_object_name = "photos"

    def get_queryset(self):
        return Photo.objects.filter(author=self.request.user)
