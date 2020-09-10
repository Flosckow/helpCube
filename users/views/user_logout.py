from django.http import JsonResponse, HttpResponse

from utils.utils import timing


@timing
def user_logout(request):
    from django.contrib.auth import logout
    logout(request)
    return JsonResponse({"url": '/'})


def reset_userdata(request):
    request.session['user-data'] = None
    return HttpResponse('user data dropped')
