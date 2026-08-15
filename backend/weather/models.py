"""
models.py

WHY: The core feature (fetching live weather) doesn't need to be stored
in our own database — it comes fresh from the OpenWeatherMap API every
time. But it's good practice to keep a small model so the project has a
real database table, and so we can show recent/popular searches later
if needed.

SearchHistory simply logs every city a user searches for, with a
timestamp. This is optional for the dashboard to function, but is used
by admin.py so you can inspect search activity in the Django admin.
"""

from django.db import models


class SearchHistory(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100, blank=True, null=True)
    searched_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-searched_at']
        verbose_name_plural = 'Search History'

    def __str__(self):
        return f"{self.city} ({self.searched_at:%Y-%m-%d %H:%M})"
