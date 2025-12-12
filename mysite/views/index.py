from django.views.generic import ListView

from models_app.models import Photo


class IndexView(ListView):
    model = Photo
    paginate_by = 6
    template_name = "index.html"
    context_object_name = "photos"
