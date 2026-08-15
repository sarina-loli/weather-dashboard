"""
admin.py

WHY: Registering SearchHistory here lets you log into /admin/ and see
every city that has been searched, when, and from which country. Useful
for debugging and for spotting popular cities.
"""

from django.contrib import admin
from .models import SearchHistory


@admin.register(SearchHistory)
class SearchHistoryAdmin(admin.ModelAdmin):
    list_display = ('city', 'country', 'searched_at')
    list_filter = ('country',)
    search_fields = ('city', 'country')
    ordering = ('-searched_at',)
