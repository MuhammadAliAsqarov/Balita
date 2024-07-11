from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
urlpatterns = [
    path('balita/admin/', admin.site.urls),
    path('balita/', include('blog.urls')),
    re_path(r'balita/static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    re_path(r'balita/media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
