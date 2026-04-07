from django.contrib.auth.views import TemplateView


class AuthView(TemplateView):
    template_name = "authorization.html"
