from django.http import HttpResponse


class SocialAuthMixin:

    @staticmethod
    def _login(request, user_soc):
        from django.contrib import auth
        auth.login(request, user_soc)
        return HttpResponse('/')
