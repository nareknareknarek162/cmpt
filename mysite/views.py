from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render


def index(request):
    return render(request, "index.html")


def authorisation_page(request):
    return render(request, "authorisation.html")


def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("index")
    else:
        return render(
            request, "authorisation.html", {"error": "Неверный логин или пароль"}
        )


def logout_view(request):
    logout(request)
    return redirect("index")
