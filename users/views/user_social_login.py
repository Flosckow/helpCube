import uuid
from urllib.request import urlopen

from django.http import HttpResponse, HttpResponseRedirect

import requests
from urllib.parse import urlencode

from users.models import User
from users.social_mixin import SocialAuthMixin
from django.views.generic import View
from django.conf import settings

from utils.utils import timing

AUTH_ERROR = "не удалось получить данные аккаунта"


class FacebookView(SocialAuthMixin, View):
    """Получаем данные пользователя с Facebook"""

    def _get_user_data(self, user_id, token):
        params = {
            "fields": "email,first_name,last_name",
            "access_token": token,
        }
        resp = requests.get(self.FB_USER_DATA_URL + urlencode(params)).json()
        return resp

    def get(self, request, *args, **kwargs):
        self.FB_APP_ID = settings.SOCIAL_FACEBOOK_ID
        self.FB_AUTH_URL = settings.SOCIAL_FACEBOOK_AUTH_URL
        self.FB_REDIRECT = settings.SOCIAL_FACEBOOK_REDIRECT_URL
        self.FB_USER_DATA_URL = settings.SOCIAL_FACEBOOK_API_URL
        self.FB_PROTECT_KEY = settings.SOCIAL_FACEBOOK_TOKEN
        self.FB_TOKEN_URL = settings.SOCIAL_FACEBOOK_TOKEN_URL

        params = {
            "client_id": self.FB_APP_ID,
            "redirect_uri": self.FB_REDIRECT,
        }
        code = request.GET.get("code")
        if code:
            try:
                params.update(
                    {
                        "client_secret": self.FB_PROTECT_KEY,
                        "code": code,
                    }
                )
                resp = requests.get(self.FB_TOKEN_URL + urlencode(params)).json()
                token = resp.get("access_token")

                params = {"access_token": token}
                resp = requests.get(self.FB_USER_DATA_URL + urlencode(params)).json()
                user_id = resp.get("id")

                if user_id:
                    user_obj = User.objects.filter(social_facebook=user_id)
                    if user_obj:
                        return self._login(request, user_obj)
                    resp["user-data"] = self._get_user_data(user_id, token)
                request.session["user-data"] = resp["user-data"]
            except Exception as e:
                request.session["user-data"] = {"error": AUTH_ERROR}
            return HttpResponseRedirect("/")
        #  При первом захлде на url отдаём на клиент
        # строку адреса дял перенаправления. Из клиентского кода
        params.update(
            {
                "auth_type": "reauthenticate",
                "scope": "email,public_profile",
                "display": "popup",
                "response_type": "code",
            }
        )

        return HttpResponse(self.FB_AUTH_URL + urlencode(params))


class GithubView(SocialAuthMixin, View):
    def _get_user_data(self, token):
        params = {"access_token": token}
        user_data = requests.get(
            self.SOCIAL_GITHUB_GET_USER_DATA + urlencode(params)
        ).json()
        user_emails = requests.get(
            self.SOCIAL_GITHUB_GET_USER_EMAIL + urlencode(params)
        ).json()
        email = ""
        name = ""

        # Получаем основной email пользователя
        for user_email in user_emails:
            if user_email["primary"]:
                email = user_email["email"]
                break

        if user_data["name"]:
            name = user_data["name"]

        return {
            "id": user_data["id"],
            "login": user_data["login"],
            "email": email,
            "name": name,
        }

    def get(self, request, *args, **kwargs):
        self.SOCIAL_GITHUB_ID = settings.SOCIAL_GITHUB_ID
        self.SOCIAL_GITHUB_SECRET = settings.SOCIAL_GITHUB_SECRET
        self.SOCIAL_GITHUB_AUTH_URL = settings.SOCIAL_GITHUB_AUTH_URL
        self.SOCIAL_GITHUB_REDIRECT_URL = settings.SOCIAL_GITHUB_REDIRECT_URL
        self.SOCIAL_GITHUB_TOKEN_URL = settings.SOCIAL_GITHUB_TOKEN_URL
        self.SOCIAL_GITHUB_GET_USER_DATA = settings.SOCIAL_GITHUB_GET_USER_DATA
        self.SOCIAL_GITHUB_GET_USER_EMAIL = settings.SOCIAL_GITHUB_GET_USER_EMAIL

        params = {
            "client_id": "7642118bb47047141802",
            "redirect_uri": "http://127.0.0.1:8000/social/github",
        }
        code = request.GET.get("code")
        if code:
            try:
                params.update(
                    {
                        "client_secret": self.SOCIAL_GITHUB_SECRET,
                        "code": code,
                    }
                )
                resp = requests.get(
                    self.SOCIAL_GITHUB_TOKEN_URL + urlencode(params),
                    headers={"accept": "application/json"},
                ).json()
                token = resp["access_token"]

                params = {"access_token": token}
                resp = requests.get(
                    self.SOCIAL_GITHUB_GET_USER_DATA + urlencode(params)
                ).json()
                user_id = resp["id"]

                if user_id:
                    user_obj = User.objects.filter(social_github=user_id)
                    if user_obj:
                        return self._login(request, user_obj)
                    user_data = self._get_user_data(token)
                    request.session["user-data"] = user_data
                return HttpResponseRedirect("/")

            except Exception as e:
                request.session["user-data"] = {"error": AUTH_ERROR}

        params.update(
            {
                "state": uuid.uuid4(),  # необязательный аргумент случайна строка
                "scope": "user",
                "response_type": "code",
            }
        )

        return HttpResponse(self.SOCIAL_GITHUB_AUTH_URL + urlencode(params))
