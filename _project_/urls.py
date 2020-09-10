from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from users.views import UserLogin

urlpatterns = [
    path('', TemplateView.as_view(template_name='landing.html'), name='landing'),
    path('login/', UserLogin.as_view(), name='login'),


    # base admin
    path('admin/', admin.site.urls),
]
