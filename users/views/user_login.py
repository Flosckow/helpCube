from django.http import JsonResponse
from django.urls import reverse
from django.views.generic.base import View

from django.contrib import auth

from users.models import User
from users.models.user_token import TokenUser
from users.utils import check_email, user_token_generator
from utils.utils import timing


class UserLogin(View):
    """ Авторизация пользвателей на сайте и регистрация """

    def __init__(self, **kwargs):
        super(UserLogin, self).__init__(**kwargs)
        self.resp = {"errors": {}, "payload": {}}

    @timing
    def get(self, request, *args, **kwargs):
        pass

    @timing
    def post(self, request, *args, **kwargs):
        return {
            "register": self._registration,
            "lost_password": self._lost_password,
            "login": self._login,
        }.get(request.POST.get("action"), self._login)(request, **kwargs)

    @timing
    def _login(self, request, **kwargs):
        """ Авторизация пользователя"""

        rpg = request.POST.get
        if not rpg("password"):
            self.resp["errors"].update({"password": "Это обязательное поле"})

        try:
            check_email(rpg("email"))
        except ValueError as e:
            self.resp["errors"].update(e.args[0])

        if not self.resp["errors"]:
            email = rpg("email")
            password = rpg("password")
            user = auth.authenticate(email=email, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                self.resp["payload"].update({"target": reverse("dashboard")})
                return JsonResponse(self.resp, status=200)
            else:
                self.resp["errors"].update({"auth_error": "Ошибка авторизации"})

        return JsonResponse(self.resp, status=403)

    def _registration(self):
        """ Регистрация пользователя"""
        pass

    def _lost_password(self):
        """ Восстановление пароля пользователя"""
        rpg = self.request.POST.get
        if rpg("email"):
            email = rpg("email")
            if User.objects.filter(email__iexact=email).exist():
                self.resp["errors"].update(
                    {"email": "Пользователь с таким email не найден"}
                )
            if TokenUser.objects.filter(user__email__iexact=email).exist():
                self.resp["errors"].update(
                    {
                        "email": "Вам уже отправлено письмо на почту. Следуйте инструкциям."
                    }
                )
            if not self.resp["errors"]:
                try:
                    token = user_token_generator()
                    user_token = TokenUser.objects.create(user=email, token=token)
                    user_token.save()
                    email_subject = f"[HelpCube] Восстановление пароля"
                except ValueError as e:
                    self.resp["errors"].update(e.args[0])
            return self.resp
        elif rpg("reset_pass"):
            if rpg("password1") != rpg("password2"):
                self.resp["errors"].update(
                    {
                        "password1": "Пароли не совпадают",
                        "password2": "Пароли не совпадают",
                    }
                )
                email = rpg("reset_email")
                if not self.resp["errors"]:
                    try:
                        token = TokenUser.objects.get(user__email__iexact=email)
                        if rpg("token") == token.token:
                            token.delete()
                            user = User.objects.get(email=email)
                            user.set_password(rpg("password1"))
                            user.save()
                        else:
                            self.resp["errors"].update(
                                {"token": "Получен не верный токен"}
                            )
                    except Exception as e:
                        self.resp["errors"].update(e.args[0])

                    resp = self._login(rpg("reset_email"), rpg("password1"))
                    self.resp["payload"].update({"target": resp.get("target")})
                return self.resp
