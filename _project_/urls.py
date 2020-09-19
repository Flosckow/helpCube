from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from _project_.views import LandingPageView
from users.views import UserLogin, FacebookView

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing'),
    path('login/', UserLogin.as_view(), name='login'),
    path('social/fb/', FacebookView.as_view()),
    path('dashboard/', TemplateView.as_view(template_name='dashboard.html'), name='dashboard'),

    # base admin
    path('admin/', admin.site.urls),

    path('ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
