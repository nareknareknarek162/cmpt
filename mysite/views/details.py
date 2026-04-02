from django.views.generic import TemplateView


class DetailedPhotoView(TemplateView):
    template_name = "details.html"
