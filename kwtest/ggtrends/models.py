from django.db import models
import uuid


class YearTrend(models.Model):
    year_trend = models.IntegerField(null=True, blank=True)
    trends = models.JSONField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.year_trend)


class TodayTrends(models.Model):
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    trend_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.trend_name


class TrendPosts(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    trend_name = models.ForeignKey(
        'TodayTrends', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    link = models.URLField(max_length=255, null=True, blank=True)
    body = models.CharField(max_length=50000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.link
