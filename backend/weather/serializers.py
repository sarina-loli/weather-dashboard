"""
serializers.py

WHY: DRF serializers do two jobs for us here:

1. CitySerializer validates the incoming `city` query parameter before
   we ever call the external OpenWeatherMap API. This stops empty or
   invalid input early, with a clean 400 error instead of a confusing
   crash further down the line.

2. SearchHistorySerializer converts SearchHistory model instances into
   JSON (used if you want to expose a "recent searches" endpoint later).
"""

from rest_framework import serializers
from .models import SearchHistory


class CitySerializer(serializers.Serializer):
    city = serializers.CharField(
        max_length=100,
        allow_blank=False,
        trim_whitespace=True,
        error_messages={
            'blank': 'City name cannot be empty.',
            'required': 'City query parameter is required, e.g. ?city=London',
        },
    )


class SearchHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchHistory
        fields = ['id', 'city', 'country', 'searched_at']
