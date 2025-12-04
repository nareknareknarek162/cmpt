from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, ListView, View

from models_app.models import Like, Photo, User


class IndexView(ListView):
    model = Photo
    paginate_by = 6
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


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ["image", "description"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4, "class": "form-control"})
        }

    def clean_description(self):
        value = self.cleaned_data.get("description", "")

        if not len(value):
            raise forms.ValidationError("Добавьте описание")

        return value

    def clean_image(self):
        image = self.cleaned_data.get("image")

        if not image:
            raise forms.ValidationError("Добавьте фото.")

        return image


class AddPhotoView(CreateView):
    model = Photo
    form_class = PhotoForm
    template_name = "add_photo.html"
    success_url = "/account"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
