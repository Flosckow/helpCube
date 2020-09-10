from django.views.generic import TemplateView

from utils.utils import timing


class UserLogin(TemplateView):
    """ User """
    template_name = 'landing.html'

    def dispatch(self, request, *args, **kwargs):
        pass

    @timing
    def get(self, request, *args, **kwargs):
        pass

    @timing
    def post(self, request, *args, **kwargs):
        pass

    @timing
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
