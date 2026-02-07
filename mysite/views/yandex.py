import requests
from django.shortcuts import render
from rest_framework.views import APIView

from config.settings.django import env


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
        return render(request, "callback.html")
