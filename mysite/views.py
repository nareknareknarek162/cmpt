from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView, View

from models_app.models import Like, Photo, User


class IndexView(ListView):
    model = Photo
    # paginate_by = 6
    template_name = "index.html"
    context_object_name = "photos"


class DetailedPhotoView(DetailView):
    model = Photo
    template_name = "details.html"
    context_object_name = "photo"

    def post(self, request, *args, **kwargs):
        self.photo = self.get_object()
        user = request.user

        if (
            not user.is_authenticated
        ):  # как запомниать незарегистрированных пользователей?
            return redirect("auth")

        already_liked = Like.objects.filter(user=user, photo=self.photo).exists()

        if not already_liked:
            Like.objects.create(user=user, photo=self.photo)

        return redirect("details", pk=self.photo.pk)


class AuthView(LoginView):
    template_name = "authorisation.html"

    def post(self, request, *args, **kwargs):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            return render(
                request, self.template_name, {"error": "Неверный логин или пароль"}
            )


class Logout(LogoutView):
    pass


class RegistrationView(View):  # Formview?
    template_name = "registrate.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        birth_date = request.POST["birth_date"]
        gender = request.POST["gender"]
        user = User(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            birth_date=birth_date,
            is_staff=False,
            is_active=True,
            gender=gender,
        )
        user.set_password(password)
        user.save()
        return redirect("index")
