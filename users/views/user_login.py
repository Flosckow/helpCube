from django.http import JsonResponse
from django.urls import reverse
from django.views.generic.base import View

from users.utils import check_email
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
            'register': self._registration,
            'lost_password': self._lost_password,
            'login': self._login
        }.get(request.POST.get('action'), self._login)(request, **kwargs)

    def _login(self, request):
        """ Авторизация пользователя"""
        if not self.kwargs.get('password'):
            self.resp["errors"].update({"password": "Это обязательное поле"})

        try:
            check_email(self.kwargs.get('email'))
        except ValueError as e:
            self.resp["errors"].update(e.args[0])

        if not self.resp['errors']:
            from django.contrib import auth
            email = self.kwargs.get('email')
            password = self.kwargs.get('password')
            user = auth.authenticate(email=email, password=password)
            if user is not None and user.is_active:
                auth.login(self.request, user)
                self.resp["payload"].update({
                    "target": reverse()
                })
            else:
                self.resp["errors"].update({"auth_error": "Ошибка авторизации"})

        return JsonResponse(self.resp)





    def _registration(self):
        """ Регистрация пользователя"""
        pass

    def _lost_password(self):
        """ Восстановление пароля """
        pass
    