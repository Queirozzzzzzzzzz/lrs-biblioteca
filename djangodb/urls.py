from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

#Caminhos/Urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'website.views.custom404'
handler500 = 'website.views.custom500'