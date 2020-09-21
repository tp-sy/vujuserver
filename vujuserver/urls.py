from django.contrib import admin
from django.urls import path, include

PROJECT_NAME = "otit32"

urlpatterns = [
    path('admin/', admin.site.urls),
    path(PROJECT_NAME + "/", include('vuju.urls')),
]
