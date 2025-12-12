from django.shortcuts import redirect, render
from django.views.generic import View

from models_app.models import User


class RegistrationView(View):
    template_name = "registrate.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        user = User(
            username=request.POST["username"],
            first_name=request.POST["first_name"],
            last_name=request.POST["last_name"],
            email=request.POST["email"],
            birth_date=request.POST["birth_date"],
            is_staff=False,
            is_active=True,
            gender=request.POST["gender"],
        )
        user.set_password(request.POST["password"])
        user.save()
        return redirect("account")
