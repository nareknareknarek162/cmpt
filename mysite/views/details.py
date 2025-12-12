from django.shortcuts import redirect
from django.utils import timezone
from django.views.generic import DetailView

from models_app.models import Comment, Like, Photo


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
            if "comment_text" in request.POST:
                comment_text = request.POST["comment_text"]
                comment = Comment(
                    author=user,
                    photo=self.get_object(),
                    text=comment_text,
                    comment_date=timezone.now(),
                )  # auto_now_add=True
                comment.save()

            if "like" in request.POST:
                if not user.is_authenticated:
                    return redirect("auth")

                obj, created = Like.objects.get_or_create(
                    user=user, photo=self.get_object()
                )

                if not created:
                    Like.objects.filter(user=user, photo=self.get_object()).delete()

            return redirect("details", pk=self.get_object().pk)
        return redirect("auth")
