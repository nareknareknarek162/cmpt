from django.views.generic import TemplateView


class AccountView(TemplateView):
    template_name = "account.html"
    context_object_name = "photos"
