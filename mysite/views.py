from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, ListView, View

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_liked"] = Like.objects.filter(
            user=self.request.user, photo=self.get_object()
        ).exists()
        return context

    def post(self, request, *args, **kwargs):
        self.photo = self.get_object()
        user = request.user

        if not user.is_authenticated:
            return redirect("auth")

        obj, created = Like.objects.get_or_create(user=user, photo=self.photo)

        if not created:
            Like.objects.filter(user=user, photo=self.photo).delete()

        return redirect("details", pk=self.photo.pk)


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


class AccountView(ListView):
    model = Photo
    # paginate_by = 6
    template_name = "account.html"
    context_object_name = "photos"

    def get_queryset(self):
        return Photo.objects.filter(author=self.request.user)


class AddPhotoView(CreateView):
    model = Photo
    fields = ["image", "description"]
    template_name = "add_photo.html"
    success_url = "/account"
