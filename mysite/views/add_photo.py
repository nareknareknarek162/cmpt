from django.views.generic import CreateView

from models_app.models import Photo
from mysite.forms.photo import PhotoForm


class AddPhotoView(CreateView):
    model = Photo
    form_class = PhotoForm
    template_name = "add_photo.html"
    success_url = "/account"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
