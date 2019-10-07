from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('listas/', include('listas.urls')),
    path('admin/', admin.site.urls),
]