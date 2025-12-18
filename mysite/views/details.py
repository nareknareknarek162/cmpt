from django.shortcuts import redirect
from django.utils import timezone
from django.views.generic import DetailView

from models_app.models import Comment, Like, Photo


class DetailedPhotoView(DetailView):
    model = Photo
    template_name = "details.html"
    context_object_name = "photo"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_liked"] = Like.objects.filter(
            user=self.request.user, photo=self.get_object()
        ).exists()

        context["comments"] = Comment.objects.filter(photo=self.get_object())
        context["users_comment"] = Comment.objects.filter(
            author=self.request.user, photo=self.get_object()
        ).first()

        context["editing"] = self.request.GET.get("edit") == "1"
        context["has_commented"] = Comment.objects.filter(
            author=self.request.user, photo=self.get_object()
        ).exists()
        return context

    def post(self, request, *args, **kwargs):
        user = request.user

        if user.is_authenticated:
            if "comment" in request.POST:
                action = request.POST["comment"]

                if action == "update":
                    Comment.objects.filter(author=user, photo=self.get_object()).update(
                        text=request.POST["comment_text"]
                    )

                elif action == "save":
                    comment_text = request.POST["comment_text"]
                    comment = Comment(
                        author=user,
                        photo=self.get_object(),
                        text=comment_text,
                        comment_date=timezone.now(),
                    )  # auto_now_add=True
                    comment.save()

                else:
                    Comment.objects.filter(
                        author=user, photo=self.get_object()
                    ).delete()

            if "like" in request.POST:

                obj, created = Like.objects.get_or_create(
                    user=user, photo=self.get_object()
                )

                if not created:
                    obj.delete()

            return redirect("details", pk=self.get_object().pk)
        return redirect("auth")
