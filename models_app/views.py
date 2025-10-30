from django.shortcuts import render


def index(request):
    return render(request, "models_app/index.html")


def authorisation(request):
    return render(request, "models_app/authorisation.html")
