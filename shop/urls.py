from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from catalog.views import home, register, login_view, create_product


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home),
    path("register/", register),
    path("login/", login_view),
    path("create/", create_product),
]


if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )