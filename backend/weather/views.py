"""
views.py

WHY: This is the HTTP layer. It:
1. Validates the incoming request using CitySerializer.
2. Delegates the actual work to services.py.
3. Logs the search into SearchHistory (models.py).
4. Translates any service-layer exceptions into proper HTTP status codes
   and JSON error messages the React frontend can display.
"""

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import CitySerializer
from .models import SearchHistory
from .services import get_weather_data, CityNotFoundError, WeatherServiceError


@api_view(['GET'])
def weather_view(request):
    """
    GET /api/weather/?city=London

    Returns current weather + hourly forecast + 5-day forecast for the
    given city, or a 404/400/502 JSON error on failure.
    """
    serializer = CitySerializer(data=request.query_params)
    if not serializer.is_valid():
        return Response(
            {'error': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    city = serializer.validated_data['city']

    try:
        data = get_weather_data(city)
    except CityNotFoundError:
        return Response(
            {'error': f'City "{city}" was not found. Please check the spelling and try again.'},
            status=status.HTTP_404_NOT_FOUND,
        )
    except WeatherServiceError as exc:
        return Response(
            {'error': str(exc)},
            status=status.HTTP_502_BAD_GATEWAY,
        )

    # Log the successful search (non-blocking best-effort logging).
    SearchHistory.objects.create(city=data['current']['city'], country=data['current']['country'])

    return Response(data, status=status.HTTP_200_OK)
