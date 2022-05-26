from django.db import models
import uuid


class VietNamTwitterTrend(models.Model):
    link = models.URLField(null=True, blank=True)
    trend_name = models.CharField(max_length=255, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.trend_name

    class Meta():
        ordering = ['trend_name']


class WorldwideTwitterTrend(models.Model):
    count = models.CharField(max_length=255, blank=True, null=True)
    link = models.URLField(null=True, blank=True)
    pos = models.IntegerField(null=True, blank=True)
    trend_name = models.CharField(max_length=255, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.trend_name

    class Meta():
        ordering = ['created']


class TopHashtagTrend(models.Model):
    link = models.URLField(null=True, blank=True)
    pos = models.IntegerField(null=True, blank=True)
    trend_name = models.CharField(max_length=255, blank=True, null=True)
    tweets = models.CharField(max_length=255, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.trend_name

    class Meta():
        ordering = ['trend_name']


class LongestTrend(models.Model):
    link = models.URLField(null=True, blank=True)
    pos = models.IntegerField(null=True, blank=True)
    trend_name = models.CharField(max_length=255, blank=True, null=True)
    tweets = models.CharField(max_length=255, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.trend_name

    class Meta():
        ordering = ['trend_name']
