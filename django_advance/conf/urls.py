from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # 追加
from django.conf.urls.static import static  # 追加

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crud/', include('crud.urls')),
    path('search/', include('search.urls')),
    path('', include('accounts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)