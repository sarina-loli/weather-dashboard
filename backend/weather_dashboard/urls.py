"""
Root URL configuration.

WHY: this file is the entry point for all URLs. It delegates anything
starting with /api/ to the `weather` app's own urls.py, keeping the
project file clean and the app self-contained.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('weather.urls')),
]
