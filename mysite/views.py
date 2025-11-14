from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from models_app.models import Photo, User


def index(request):
    photos = Photo.objects.all()
    return render(request, "index.html", {"photos": photos})


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


def registration_view(request):
    return render(request, "registrate.html")


def registrate_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    email = request.POST["email"]
    birth_date = request.POST["birth_date"]
    gender = request.POST["gender"]
    user = User(username=username, first_name=first_name, last_name=last_name, email=email, birth_date=birth_date,
                is_staff=False, is_active=True, gender=gender)
    user.set_password(password)
    user.save()
    return redirect("index")
