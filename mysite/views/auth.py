from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render


class AuthView(LoginView):
    template_name = "authorisation.html"

    def post(self, request, *args, **kwargs):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("account")
        else:
            return render(
                request, self.template_name, {"error": "Неверный логин или пароль"}
            )


class Logout(LogoutView):
    pass
