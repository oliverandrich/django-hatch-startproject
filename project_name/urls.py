# URL Configuration
# https://docs.djangoproject.com/en/4.1/topics/http/urls/

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    # Out urls
    path("", TemplateView.as_view(template_name="base.html")),
    # Admin area
    path(settings.ADMIN_URL, admin.site.urls),
    # Django browser reload
    path("__reload__/", include("django_browser_reload.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
