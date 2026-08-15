"""
urls.py (weather app)

WHY: Keeps the weather app's routes self-contained. The project's root
urls.py includes this file under the /api/ prefix, so the final route
is: GET /api/weather/?city=London
"""

from django.urls import path
from .views import weather_view

urlpatterns = [
    path('weather/', weather_view, name='weather'),
]
