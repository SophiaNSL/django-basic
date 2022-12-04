from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve

from hello.views import hello_world
from my_project import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include('hello.urls')),
    path('accounts/', include('accounts.urls')),

]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
