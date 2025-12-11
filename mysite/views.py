from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, ListView, View

from models_app.models import Comment, Like, Photo, User
from mysite.forms.photo import PhotoForm


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
        context["comments"] = Comment.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        user = request.user

        if user.is_authenticated:
            self.photo = self.get_object()
            if "comment_text" in request.POST:
                comment_text = request.POST["comment_text"]
                comment = Comment(author=user, photo=self.photo, text=comment_text)
                comment.save()

            if "like" in request.POST:
                if not user.is_authenticated:
                    return redirect("auth")

                obj, created = Like.objects.get_or_create(user=user, photo=self.photo)

                if not created:
                    Like.objects.filter(user=user, photo=self.photo).delete()

            return redirect("details", pk=self.photo.pk)
        return redirect("auth")


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
    form_class = PhotoForm
    template_name = "add_photo.html"
    success_url = "/account"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
