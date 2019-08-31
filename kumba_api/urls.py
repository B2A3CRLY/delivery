from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from backend.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('backend.urls')),
    path('api/', include('users.urls')),
    path("", index, name="home"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
