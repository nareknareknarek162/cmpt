import requests
from django.contrib.auth import login
from django.shortcuts import redirect
from rest_framework.views import APIView

from config.settings.django import env
from models_app.models import User


class Yandex(APIView):

    def get(self, request):
        code = request.query_params["code"]
        client_id = env("OAUTH_CLIENT_ID", cast=str)
        client_secret = env("OAUTH_CLIENT_SECRET", cast=str)

        url = "https://oauth.yandex.ru/token"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
        }
        data = {
            "grant_type": "authorization_code",
            "code": code,
            "client_id": client_id,
            "client_secret": client_secret,
        }

        response = requests.post(url, headers=headers, data=data)
        data = response.json()

        access_token = data["access_token"]

        user_data = requests.get(
            f"https://login.yandex.ru/info?oauth_token={access_token}"
        ).json()
        user, created = User.objects.get_or_create(
            id=user_data["id"],
            defaults={
                "username": user_data["login"],
                "first_name": user_data["first_name"],
                "last_name": user_data["last_name"],
                "email": user_data["default_email"],
                "birth_date": user_data["birthday"],
                "is_staff": False,
                "is_active": True,
                "gender": user_data["sex"][0].upper(),
            },
        )

        if created:
            user.set_unusable_password()
            user.save()
        login(request, user)

        return redirect("account")
