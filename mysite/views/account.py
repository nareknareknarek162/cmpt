from django.views.generic import TemplateView


class AccountView(TemplateView):
    template_name = "account.html"
