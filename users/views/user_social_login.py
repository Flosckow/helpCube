from urllib.request import urlopen

from django.http import HttpResponse, HttpResponseRedirect

import requests
from urllib.parse import urlencode

from users.models import User
from users.social_mixin import SocialAuthMixin
from django.views.generic import View
from django.conf import settings


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
